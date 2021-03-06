import os
import sys

ABSPATH = os.path.abspath(os.path.realpath(os.path.dirname(__file__)) + "/..")
sys.path.append(ABSPATH)
import asposecellscloud
from asposecellscloud.rest import ApiException
from asposecellscloud.apis.cells_api import CellsApi
import AuthUtil
from asposecellscloud.models import CalculationOptions
from asposecellscloud.models import FontSetting
from asposecellscloud.models import Font
from asposecellscloud.models import Style


api_client = AuthUtil.GetApiClient()
api = asposecellscloud.apis.cells_api.CellsApi(api_client)
        name ='myDocument.xlsx'
        sheet_name ='Sheet3'
        chartIndex = 0  
        title = Title()
        title.text = "test"
        folder = "Temp"
        AuthUtil.Ready(name, folder)
        result = self.api.cells_charts_post_worksheet_chart_title(name, sheet_name, chartIndex , title = title, folder=folder)