from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from intrahospital_api.apis import get_api
from collections import defaultdict, OrderedDict
from opal.core.views import json_response


class StaffRequiredMixin(object):
    @method_decorator(staff_member_required)
    def dispatch(self, *args, **kwargs):
        return super(StaffRequiredMixin, self).dispatch(*args, **kwargs)


def pivot_data(raw_data):
    # pivot the row data to make it easy to read
    row_data_dict = defaultdict(list)

    for row in raw_data:
        for key, value in row.items():
            row_data_dict[key].append(value)

    for key, row in row_data_dict.items():
        row.insert(0, key)
    pivotted = row_data_dict.values()
    return sorted(pivotted, key=lambda x: x[0].upper())


class PivottedData(StaffRequiredMixin, TemplateView):
    template_name = "intrahospital_api/table_view.html"
    api_method = ""

    def get_context_data(self, *args, **kwargs):
        api = get_api()
        ctx = super(PivottedData, self).get_context_data(
            *args, **kwargs
        )
        raw_data = getattr(api, self.api_method)(kwargs["hospital_number"])
        row_data = pivot_data(raw_data)
        row_data = sorted(list(row_data), key=lambda x: x[0])
        ctx["row_data"] = row_data
        return ctx


class IntrahospitalRawView(PivottedData):
    api_method = "raw_data"

    def get_context_data(self, *args, **kwargs):
        ctx = super(IntrahospitalRawView, self).get_context_data(
            *args, **kwargs
        )
        ctx["title"] = "All Raw Data"
        return ctx


class IntrahospitalCookedView(PivottedData):
    api_method = "cooked_data"

    def get_context_data(self, *args, **kwargs):
        ctx = super(IntrahospitalCookedView, self).get_context_data(
            *args, **kwargs
        )
        ctx["title"] = "All Cooked Data"
        return ctx


class IntrahospitalRawResultsView(StaffRequiredMixin, TemplateView):
    """
        Provides the raw results, remove cerner fields as these are demographics
         grouped by lab number, observation id
    """
    template_name = "intrahospital_api/raw_result_view.html"

    def get_context_data(self, *args, **kwargs):
        ctx = super(IntrahospitalRawResultsView, self).get_context_data(
            *args, **kwargs
        )
        api = get_api()

        results = api.raw_data(
            **self.kwargs
        )
        results = sorted(
            results, key=lambda x: x["OBX_exam_code_Text"]
        )
        ctx["lab_results"] = defaultdict(list)

        for result in results:
            row = ((i, v,) for i, v in result.items() if not i.startswith("CRS_"))
            row = OrderedDict(sorted(row, key=lambda x: x[0]))
            ctx["lab_results"][result["Result_ID"]].append(row)

        for lab_number, result in ctx["lab_results"].items():
            ctx["lab_results"][lab_number] = pivot_data(
                ctx["lab_results"][lab_number]
            )

        # django templates don't like default dicts
        ctx["lab_results"] = dict(ctx["lab_results"])

        ctx["title"] = "Raw Results Data"
        return ctx


class IntrahospitalCookedResultsView(StaffRequiredMixin, TemplateView):
    template_name = "intrahospital_api/cooked_result_view.html"

    def get_context_data(self, *args, **kwargs):
        ctx = super(IntrahospitalCookedResultsView, self).get_context_data(
            *args, **kwargs
        )
        api = get_api()
        ctx["lab_results"] = api.results_for_hospital_number(
            kwargs["hospital_number"], **self.request.GET
        )
        ctx["title"] = "Cooked Results Data"
        return ctx


@staff_member_required
def results_as_json(request, *args, **kwargs):
    api = get_api()
    results = api.results_for_hospital_number(
        kwargs["hospital_number"], **request.GET
    )
    return json_response(results)
