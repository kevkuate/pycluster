import simplejson
import jsonpickle
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash, make_response, jsonify, Markup, Response


def graph_line(pluginData, func_name, func_nfo):
    """
    converts from the original format to highcharts format. returning the JSON
    """
    #"#Base\t%GC",
    #"1\t40.209569984588065",
    #"2\t39.756647339140365",

    #//categoriesX = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10-14', '15-19', '20-24', '25-29', '30-34', '35-39', '40-44', '45-49'];
    #//data        = [{
    #//                name: 'Tokyo',
    #//                data: [7.0, 6.9, 9.5, 14.5, 18.2, 21.5, 25.2, 26.5, 23.3, 18.3, 13.9, 9.6]
    #//            }, {
    #//                name: 'New York',
    #//                data: [-0.2, 0.8, 5.7, 11.3, 17.0, 22.0, 24.8, 24.1, 20.1, 14.1, 8.6, 2.5]
    #//            }, {
    #//                name: 'Berlin',
    #//                data: [-0.9, 0.6, 3.5, 8.4, 13.5, 17.0, 18.6, 17.9, 14.3, 9.0, 3.9, 1.0]
    #//            }, {
    #//                name: 'London',
    #//                data: [3.9, 4.2, 5.7, 8.5, 11.9, 15.2, 17.0, 16.6, 14.2, 10.3, 6.6, 4.8]
    #//            }];
    #//
    #//title    = "Relative Enrichment Over Read Length";
    #//subTitle = "FastQC Report";
    #//titleY   = "%";
    #//unityY   = "%";
    #//titleX   = "Position in Read (bp)"
    #//unityX   = "bp";
    #function graph_lines(data, container, title, subTitle, titleY, unityY, titleX, unityX, categoriesX) {

    lists       = []
    categoriesX = []
    dataD       = {}

    title, subTitle, titleY, unityY, titleX, unityX, minY, maxY, minX, maxX = func_nfo

    print "graph_line ",
    print func_nfo

    for line in pluginData:
        #print line
        cols = line.split('\t')
        if cols[0][0] == "#":
            lists = []
            #titleY = cols[0][1:]
            #titleX = cols[1]
            for colName in cols:
                lists.append(colName)
        else:
            categoriesX.append(str(cols[0]))
            for colIndex in range(len(cols)):
                if colIndex == 0:
                    continue

                try:
                    colVal  = float(cols[colIndex])
                except ValueError:
                    colVal  =       cols[colIndex]

                colName = lists[colIndex]
                if colName in dataD:
                    dataD[colName].append(colVal)
                else:
                    dataD[colName] = [ colVal ]

    data = []
    for colName, colData in dataD.items():
        data.append({
            'name': colName,
            'data': colData
            })

    res = {
        'categoriesX' : categoriesX,
        'data'        : data,
        'title'       : title,
        'subTitle'    : subTitle,
        'titleY'      : titleY,
        'unityY'      : unityY,
        'titleX'      : titleX,
        'unityX'      : unityX,
        'minY'        : minY,
        'maxY'        : maxY,
        'minX'        : minX,
        'maxX'        : maxX,
        '_dst_func'   : 'graph_lines',
    }

    #print res

    return jsonpickle.encode(res)

def candle_stick(pluginData, func_name, func_nfo):
    """
    converts from the original format to highcharts format. returning the JSON
    """
    #"Per base sequence quality": {
    # "data": [
    #    0     1     2       3               4               5                6
    #  "#Base\tMean\tMedian\tLower Quartile\tUpper Quartile\t10th Percentile\t90th Percentile",
    #  "1\t36.064507832356185\t37.0\t37.0\t40.0\t28.0\t40.0",
    #  "2\t35.4651882904503\t37.0\t35.0\t40.0\t25.0\t40.0",
    #  "3\t35.13829905728201\t37.0\t34.0\t40.0\t24.0\t40.0",
    #  "4\t34.98659335540772\t37.0\t34.0\t40.0\t24.0\t40.0",
    #  "5\t34.9416264163553\t37.0\t34.0\t40.0\t23.0\t40.0",

    #//[1131926400000,61.54,61.98,60.91,61.45],
    #//[1132012800000,61.60,63.08,61.46,62.28],
    #//[1132099200000,63.15,65.06,63.09,64.95],
    #//[1347321600000,665.27,670.10,656.55,660.59],
    #                 open high     low close

    title, subTitle, titleY, unityY, titleX, unityX, minY, maxY, minX, maxX = func_nfo

    print func_nfo

    data1 = []
    data2 = []
    data3 = []
    data4 = []
    for line in pluginData:
        #print line
        cols = line.split('\t')
        if cols[0][0] == "#":
            continue
        else:
            #print "'%s'" % line
            pos     = cols[0]
            dashPos = pos.find('-')

            if dashPos != -1:
                pos = float( int( pos[:dashPos] ) + int(pos[dashPos+1:]) ) / 2.0
                #print "%d + %d = %d" % (int( pos[:dashPos] ), int(pos[dashPos+1:]), posf)
                #pos = posf
            pos = int(pos)

            data1.append([ pos, float(cols[3]), float(cols[4]) ])
            data2.append([ pos, float(cols[5]), float(cols[6]) ])
            data3.append([ pos, float(cols[1])                 ])
            data4.append([ pos, float(cols[2])                 ])



    res = {
        #'categoriesX' : categoriesX,
        'data1'       : data1,
        'data2'       : data2,
        'data3'       : data3,
        'data4'       : data4,
        'title'       : title,
        'subTitle'    : subTitle,
        'titleY'      : titleY,
        'unityY'      : unityY,
        'titleX'      : titleX,
        'unityX'      : unityX,
        'minY'        : minY,
        'maxY'        : maxY,
        'minX'        : minX,
        'maxX'        : maxX,
        '_dst_func'   : 'graph_candle',
    }

    return jsonpickle.encode(res)

def stacked(pluginData, func_name, func_nfo):
    """
    converts from the original format to highcharts format. returning the JSON
    """
    #var categoriesX = ['Apples', 'Oranges', 'Pears', 'Grapes', 'Bananas'];
    #var data        = [{
    #        name: 'John',
    #        data: [5, 3, 4, 7, 2]
    #    }, {
    #        name: 'Jane',
    #        data: [2, 2, 3, 2, 1]
    #    }, {
    #        name: 'Joe',
    #        data: [3, 4, 4, 2, 5]
    #    }];

    #"contaminationData": {
    # "EcoliM": [
    #  99.66,
    #  0.0,
    #  0.12,
    #  0.08,
    #  0.14
    # ],


    lists       = []
    categoriesX = []
    categoriesY = []
    data        = []

    title, subTitle, titleY, unityY, titleX, unityX, minY, maxY, minX, maxX = func_nfo

    print func_nfo

    for spp_name in sorted(pluginData):
        values = pluginData[spp_name]
        if spp_name[0] == "_":
            categoriesY = values

    if len(categoriesY) == 0:
        categoriesY = ['%Unmapped', '%One hit one library', '%Multiple hits one library', '%One hit multiple libraries', '%Multiple hits multiple libraries']

    dataD = {}
    for spp_name in sorted(pluginData):
        values = pluginData[spp_name]
        categoriesX.append(spp_name)

        for pos in range(len(values)):
            y_label = categoriesY[pos]
            if y_label not in dataD:
                dataD[y_label] = []
            dataD[y_label].append(values[pos])
            #if spp_name[0] != "_":
            #    data.append({
            #        'name': spp_name,
            #        'data': values
            #        })
            #else:
            #    categoriesX = values

    for y_label in dataD:
        data.append({
            'name': y_label,
            'data': dataD[y_label]
            })

    res = {
        'categoriesX' : categoriesX,
        'data'        : data,
        'title'       : title,
        'subTitle'    : subTitle,
        'titleY'      : titleY,
        'unityY'      : unityY,
        'titleX'      : titleX,
        'unityX'      : unityX,
        'minY'        : minY,
        'maxY'        : maxY,
        'minX'        : minX,
        'maxX'        : maxX,
        '_dst_func'   : 'graph_stacked',
    }

    return jsonpickle.encode(res)







def parseGraph(projectName, projectStatus, projectSample, sequenceTech, libraryName, fileName, pluginName, pluginKey, pluginValue):
    """
    parse the graph request returning the icon, link and JSON url according to the data
    """
    res = []

    """
    get URL safe names to be added as parameters
    """
    lnkConstLst = []
    for kv in ( [ 'projectName',   Markup.escape( projectName   ) ],
                [ 'projectStatus', Markup.escape( projectStatus ) ],
                [ 'projectSample', Markup.escape( projectSample ) ],
                [ 'sequenceTech',  Markup.escape( sequenceTech  ) ],
                [ 'libraryName',   Markup.escape( libraryName   ) ],
                [ 'fileName',      Markup.escape( fileName      ) ],
                [ 'pluginName',    Markup.escape( pluginName    ) ],
                [ 'pluginKey',     Markup.escape( pluginKey     ) ],
                ):
        lnkConstLst.append("=".join(kv))
    lnkConst = "&".join(lnkConstLst)




    url_for_download  = url_for('download'  )
    url_forfullscreen = url_for('fullscreen')
    if isinstance(pluginValue, dict):
        """
        if dict, it means we have more than one picture here.
        """
        res.append("<table>")
        res.append("    <tr>")

        if (pluginName, pluginKey, None) in graph_mapper:
            """
            if IMAGENAME is None in mapper, it means there's only one picture and no Icon.
            add standard icon
            """
            lnk  = "%s?%s&srctype=json" % (url_for_download , lnkConst)
            href = "%s?%s&srctype=json" % (url_forfullscreen, lnkConst)
            res.append("""<a href="%(href)s" lnk="%(lnk)s" class="graphjson" title="%(title)s" target="_blank">%(dsc)s</a></td>""" %\
                        { 'href': href, 'lnk': lnk, 'title': pluginKey, 'dsc': '<i class="icon-picture"/>' })

        else:
            for imageName in pluginValue:
                """
                for each image in this plugin:
                - add icon if present
                - if raw data, add link to JSON, else, add link to image
                """

                imgdownload = "%s?%s&imageName=%s&srctype=" % (url_for_download , lnkConst, imageName)
                imgfullscre = "%s?%s&imageName=%s&srctype=" % (url_forfullscreen, lnkConst, imageName)


                dsc = Markup.escape(imageName)
                if 'ico' in pluginValue[imageName]:
                    ico_name    = 'pluginsIcons/' + pluginName + '/' + pluginValue[imageName]['ico'].replace(" ", "_").lower() + '.png'
                    url_for_ico = url_for('static', filename=ico_name)
                    dsc         = '<img src="%(url)s" class="icon">' % { 'url': url_for_ico }
                else:
                    dsc = '<i class="icon-picture"/>'


                fmtdsc = { 'title': imageName, 'dsc': dsc, 'urldown': imgdownload, 'urlfull': imgfullscre }


                if (pluginName, pluginKey, imageName) in graph_mapper and \
                'data' in pluginValue[imageName] and \
                pluginValue[imageName]['data'] is not None:
                    fmtdsc['outtype'] = 'json'

                else:
                    if 'img' in pluginValue[imageName] and pluginValue[imageName]['img'] is not None:
                        fmtdsc['outtype'] = 'img'

                if 'outtype' in fmtdsc:
                    res.append("""      <td><a href="%(urlfull)s%(outtype)s" lnk="%(urldown)s%(outtype)s" class="graph%(outtype)s" title="%(title)s" target="_blank">%(dsc)s</a></td>""" % fmtdsc)
                else:
                    res.append("""      <td title="%(title)s">%(dsc)s</td>""" % fmtdsc)

        res.append("    </tr>")
        res.append("</table>")

    else:
        lnk = "%s?%s" % (url_for_download, lnkConst)
        #res.append("""<td><img src="%s" class="graphSmall" title="%s"/></td>""" % (lnk, pluginKey))
        #res.append("""<td><a href="%s" class="graph" title="%s" target="_blank">%s</a></td>""" % (lnk, pluginKey, pluginKey))
        res.append("""<a href="%(lnk)s" class="graphimg" title="%(title)s" target="_blank">%(dsc)s</a>""" % \
                   { 'lnk': lnk, 'title': pluginKey, 'dsc': '<i class="icon-picture"/>'})

    return "\n".join(res)


#TODO: make global
graph_mapper = {
    #                                                                         parser func , graph parser js,   title,                                                 subTitle,      titleY,          , unityY, titleX               , unityX, miny, maxy, minx, maxx
    ('fastqc'       , 'fastqcGraphs'      , 'Sequence Duplication Levels' ): [graph_line  , 'graph_lines' , [ 'Sequence Duplication Levels >=38.4%'                , "FastQC"      , "Perc (%)"       , ""    , "Duplication Level"  , "x"   ,    0,  100, None, None ] ],
    ('fastqc'       , 'fastqcGraphs'      , 'Per base sequence content'   ): [graph_line  , 'graph_lines' , [ 'Sequence Content Across all Bases'                  , "FastQC"      , "Perc (%)"       , ""    , "Position in Read"   , "bp"  ,    0,  100, None, None ] ],
    ('fastqc'       , 'fastqcGraphs'      , 'Per sequence GC content'     ): [graph_line  , 'graph_lines' , [ 'GC Distribution Over all Sequences'                 , "FastQC"      , "Num Sequences"  , ""    , "Mean GC Content (%)", ""    ,    0, None, None, None ] ],
    ('fastqc'       , 'fastqcGraphs'      , 'Sequence Length Distribution'): [graph_line  , 'graph_lines' , [ 'Distribution of sequence Lengths Over all Sequences', "FastQC"      , "Num Sequences"  , ""    , "Sequence Length"    , "bp"  ,    0, None, None, None ] ],
    ('fastqc'       , 'fastqcGraphs'      , 'Per base GC content'         ): [graph_line  , 'graph_lines' , [ 'GC Content Across all Bases'                        , "FastQC"      , "Perc (%)"       , ""    , "Position in Read"   , "bp"  ,    0,  100, None, None ] ],
    ('fastqc'       , 'fastqcGraphs'      , 'Per sequence quality scores' ): [graph_line  , 'graph_lines' , [ 'Quality Score Distribution Over all Sequences'      , "FastQC"      , "Num Sequences"  , ""    , "Position in Read"   , "bp"  ,    0, None, None, None ] ],
    ('fastqc'       , 'fastqcGraphs'      , 'Per base N content'          ): [graph_line  , 'graph_lines' , [ 'N Content Across all Bases'                         , "FastQC"      , "Perc (%)"       , ""    , "Position in Read"   , "bp"  ,    0,  100, None, None ] ],
    ('fastqc'       , 'fastqcGraphs'      , 'Per base sequence quality'   ): [candle_stick, 'candle_stick', [ 'Quality Scores Across all Bases'                    , "FastQC"      , "Quality (Q)"    , ""    , "Position in Read"   , "bp"  ,    0,   42, None, None ] ],
    ('contamination', 'contaminationData' , None                          ): [stacked     , 'stacked'     , [ 'Contamination'                                      , "FastQ Screen", "Perc Mapped (%)", ""    , "Species Db"         , ""    , None, None, None, None ] ],
    #('fastqc'       , 'fastqcGraphs'      , 'Kmer Content'                ): [graph_line  , 'graph_lines' ],
    #over represented sequences
    #('contamination', 'contaminationGraph', None                          ): [stacked     , 'stacked'     , ['contaminationGraph'                                 , "FastQ Screen", "Perc"           , "%", "Number", "#"] ],
}
