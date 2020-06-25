import requests



user = "admin"
password = "fmdemoadmin"
app_author = "admin"
app_name = "fmDemo"
dashboard_name = "new_testPython_dashboard_www2"
dashboard_label = "fmdemo_python_test_www2"
dashboard_description = "Dashboard for FMDEMO"
hostName = "www2"

dashboard_xml_data_vars = "<dashboard><label>" + dashboard_label + "</label><description>" + dashboard_description + \
    "</description><fieldset submitButton=\"false\"><input type=\"time\" token=\"field1\"><label>FMDEMOTimeRange</label><default><earliest>-7d@h</earliest><latest>now</latest></default></input></fieldset><row><panel><title>Request Type Count</title><table><search><query>sourcetype=access_* | chart count BY method</query><earliest>$field1.earliest$</earliest><latest>$field1.latest$</latest><sampleRatio>1</sampleRatio></search><option name=\"count\">20</option><option name=\"dataOverlayMode\">none</option><option name=\"drilldown\">none</option><option name=\"percentagesRow\">false</option><option name=\"refresh.display\">progressbar</option><option name=\"rowNumbers\">false</option><option name=\"totalsRow\">false</option><option name=\"wrap\">true</option></table></panel><panel><title>Top Purchases By Category</title><chart><search><query>sourcetype=access_* status=200 action=purchase | top categoryId</query><earliest>$field1.earliest$</earliest><latest>$field1.latest$</latest><sampleRatio>1</sampleRatio></search><option name=\"charting.axisLabelsX.majorLabelStyle.overflowMode\">ellipsisNone</option><option name=\"charting.axisLabelsX.majorLabelStyle.rotation\">0</option><option name=\"charting.axisTitleX.visibility\">visible</option><option name=\"charting.axisTitleY.visibility\">visible</option><option name=\"charting.axisTitleY2.visibility\">visible</option><option name=\"charting.axisX.abbreviation\">none</option><option name=\"charting.axisX.scale\">linear</option><option name=\"charting.axisY.abbreviation\">none</option><option name=\"charting.axisY.scale\">linear</option><option name=\"charting.axisY2.abbreviation\">none</option><option name=\"charting.axisY2.enabled\">0</option><option name=\"charting.axisY2.scale\">inherit</option><option name=\"charting.chart\">pie</option><option name=\"charting.chart.bubbleMaximumSize\">50</option><option name=\"charting.chart.bubbleMinimumSize\">10</option><option name=\"charting.chart.bubbleSizeBy\">area</option><option name=\"charting.chart.nullValueMode\">gaps</option><option name=\"charting.chart.showDataLabels\">none</option><option name=\"charting.chart.sliceCollapsingThreshold\">0.01</option><option name=\"charting.chart.stackMode\">default</option><option name=\"charting.chart.style\">shiny</option><option name=\"charting.drilldown\">none</option><option name=\"charting.layout.splitSeries\">0</option><option name=\"charting.layout.splitSeries.allowIndependentYRanges\">0</option><option name=\"charting.legend.labelStyle.overflowMode\">ellipsisMiddle</option><option name=\"charting.legend.mode\">standard</option><option name=\"charting.legend.placement\">right</option><option name=\"charting.lineWidth\">2</option><option name=\"refresh.display\">progressbar</option><option name=\"trellis.enabled\">0</option><option name=\"trellis.scales.shared\">1</option><option name=\"trellis.size\">medium</option></chart></panel><panel><title>Status Code Count by Host (" + \
    hostName + ")</title><table><search><query>sourcetype=access_* host=" + hostName + " | chart count BY status</query><earliest>$field1.earliest$</earliest><latest>$field1.latest$</latest><sampleRatio>1</sampleRatio></search><option name=\"count\">20</option><option name=\"dataOverlayMode\">none</option><option name=\"drilldown\">none</option><option name=\"percentagesRow\">false</option><option name=\"refresh.display\">progressbar</option><option name=\"rowNumbers\">false</option><option name=\"totalsRow\">false</option><option name=\"wrap\">true</option></table></panel></row><row><panel><title>Status Count by Host</title><table><search><query>sourcetype=access_* | chart count BY status, host</query><earliest>$field1.earliest$</earliest><latest>$field1.latest$</latest><sampleRatio>1</sampleRatio></search><option name=\"count\">20</option><option name=\"dataOverlayMode\">none</option><option name=\"drilldown\">none</option><option name=\"percentagesRow\">false</option><option name=\"refresh.display\">progressbar</option><option name=\"rowNumbers\">false</option><option name=\"totalsRow\">false</option><option name=\"wrap\">true</option></table></panel></row></dashboard>"


data = {'output_mode': 'json',
        'name': dashboard_name,
        'eai:data': dashboard_xml_data_vars
        }


response = requests.post('https://localhost:8089/servicesNS/' + app_author + '/' + app_name + '/data/ui/views/', data=data,
                         auth=(user, password), verify=False)

print(response)
