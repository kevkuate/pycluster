#!/usr/bin/python
import sys,os
import re
import pprint
import time
import base64
import datetime
import time
import simplejson
import jsonpickle
import multiprocessing
from Queue import Empty
import signal

sys.path.insert(0, 'lib')

import clustertools
import clusterclasses

setupfile    = 'uisetup.json'

if not os.path.exists(setupfile):
    print "count not find setup file %s" % setupfile
    sys.exit(1)

for k,v in jsonpickle.decode(open(setupfile, 'r').read())['server'].items():
    #print "SERVER K %s V %s" % (k, v)
    globals()[k] = v

for k,v in jsonpickle.decode(open(setupfile, 'r').read())['datas' ].items():
    #print "DATAS K %s V %s" % (k, v)
    globals()[k] = v


def start_background():
    M           = multiprocessing.Manager()
    Q           = M.Queue()

    pool = multiprocessing.Pool(2, init_worker)
        
    print "calling listener"
    app_list = pool.apply_async(listen_broadcast, args=(Q, ))
    
    time.sleep(SLEEP_FOR_BROADCAST)
    
    print "calling broadcast"
    app_broa = pool.apply_async(start_broadcast,  args=(Q, ))

   
    #while(True):
    #    try:
    #        while not q.empty():
    #            data = q.get(timeout=0.3)
    #            print "server got broadcast result:",data
    #    except Empty:
    #        pass
    #    time.sleep(1)
   
    print "sleeping"
    try:
        while(True):
            time.sleep(1)
            
    except KeyboardInterrupt:
        pool.terminate()
        pool.join()
        
    finally:
        pool.close()
        pool.join()
    
    print "bye"



def start_broadcast(q):
    print "initializing broadcast"
    broadcaster = clustertools.broadcast_sender()

    try:
        while (True):
            #print "calling broadcast"
            broadcaster.broadcastserverinfo()
            #print "broadcasted. sleeping"
            time.sleep(BROADCAST_INTERVAL)
            
    except KeyboardInterrupt:
        raise KeyboardInterrupError

    return 0

def listen_broadcast(q):
    print "initializing broadcast listening"
    broadcaster = clustertools.broadcast_receiver()
    
    try:
        while (True):
            #print "calling broadcast listener"
            data = broadcaster.listenbroadcastserverinfo()
            q.put(data)
            #print "listened. sleeping"
            
    except KeyboardInterrupt:
        raise KeyboardInterrupError

    return 0

class KeyboardInterrupError(Exception): pass
def init_worker():
    signal.signal(signal.SIGINT, signal.SIG_IGN)
    pass





def main():
    start_background()


if __name__ == '__main__':
    main()











#APPLICATION CODE :: SETUP
#@app.before_request
#def before_request():
#    """
#    before each request, add global variables to the global G variable.
#    If using WSGI (eg. apache), this wont work
#    """
#    global enterprise
#    g.enterprise = enterprise
#
#    if setupDB is None:
#        """
#        if DB not loaded yet, redirect to the LOADING.HTML page which will request through a LINK tag
#        for the initial page. As the request is caming FROM the LOADING page, we will read the db to
#        memory. The LOADING.HTML will refresh every second. When SETUPDB is finally loaded the page will
#        be redirected to the initial page
#        """
#        if request.path != "/loading":
#            print "redirecting"
#            return render_template('loading.html')
#        else:
#            g.setupDB, g.projects, g.structure, g.projectDescription, g.projectStatuses, g.plugins = getDb()
#            return redirect( url_for('initial') )
#
#    g.setupDB, g.projects, g.structure, g.projectDescription, g.projectStatuses, g.plugins = getDb()
#
#
#@app.after_request
#def after_request(response):
#    return response
#
#
#@app.teardown_request
#def teardown_request(exception):
#    pass
#
#
##APPLICATION CODE :: ROUTE
#@app.route("/loading", methods=['GET'])
#@templated("loading.html")
#def loading():
#    """
#    Show the LOADING message while loading the SETUPDB
#    """
#    return dict()
#
#@app.route('/', methods=['GET'])
#@templated('display_normal.html')
#def initial():
#    """
#    shows the start page
#    """
#    return dict()
#
#
#@app.route('/query', methods=['GET'])
#def query():
#    """
#    shows the result for the query
#    """
#    projectName = request.args.get('projectName', '')
#    return render_template('response.html', projectName=projectName)
#
#
#@app.route('/configure', methods=['POST', 'GET'])
#def configure():
#    """
#    allows to see and change the configuration.
#    GET  : show the setup
#    POST : changes the setup (FUTURE)
#    OTHER: show front pate
#    """
#    if  request.method == "GET":
#        resTemp = render_template('setup_form.html')
#        return resTemp
#
#    elif request.method == "POST":
#        resTemp = render_template('setup_form.html')
#        return resTemp
#
#    else:
#        print "INVALID REQUEST", request
#
#    return render_template('display_normal.html')
#
#
#@app.route('/download', methods=['GET'])
#def download():
#    """
#    Dowload data. either JSON or Image.
#    checks if all information have been sent and if the information is present returning 404 otherwise.
#    """
#    projectName   = request.args.get('projectName'  , None)
#    projectStatus = request.args.get('projectStatus', None)
#    projectSample = request.args.get('projectSample', None)
#    sequenceTech  = request.args.get('sequenceTech' , None)
#    libraryName   = request.args.get('libraryName'  , None)
#    fileName      = request.args.get('fileName'     , None)
#    pluginName    = request.args.get('pluginName'   , None)
#    pluginKey     = request.args.get('pluginKey'    , None)
#    imageName     = request.args.get('imageName'    , None)
#    srctype       = request.args.get('srctype'      , None)
#
#    for var in [projectName, projectStatus, projectSample, sequenceTech, libraryName, fileName, pluginName, pluginKey]:
#        """
#        returns 404 if any variable was not defined
#        """
#        if var is None:
#            print "none var"
#            abort(404)
#
#    try:
#        """
#        tries to get the result. if not found in the database, return 404
#        """
#        data    = g.structure[projectName][projectStatus][projectSample][sequenceTech][libraryName][fileName]
#    except:
#        print "no data"
#        abort(404)
#
#    #print request.headers
#
#    plugins = data.getPlugins()
#    if pluginName in plugins:
#        pluginData = data.getPlugin(pluginName)
#        if pluginKey in pluginData:
#            pluginImages = pluginData[pluginKey]
#            pluginImage  = None
#            pluginData   = None
#
#            if isinstance(pluginImages, dict):
#                if imageName is not None:
#                    if imageName in pluginImages:
#                        if srctype is None or srctype == 'img':
#                            """
#                            if image has been requested, returns it using using the correct plugin
#                            """
#                            if 'img' in pluginImages[imageName]:
#                                print "valid image key %s" % imageName
#                                pluginImage = pluginImages[imageName]['img']
#                            else:
#                                print "no such image key %s" % imageName
#                                abort(404)
#
#                        elif srctype is not None and srctype == 'json':
#                            """
#                            if json has been requested, returns it using using the correct plugin
#                            """
#                            if 'data' in pluginImages[imageName]:
#                                print "valid image key %s" % imageName
#                                pluginData = pluginImages[imageName]['data']
#                            else:
#                                print "no such image key %s" % imageName
#                                abort(404)
#
#                        else:
#                            print "no such data key %s to src type %s" % (imageName, srctype)
#                            abort(404)
#
#                    else:
#                        print "no such image %s" % imageName
#                        abort(404)
#
#                elif srctype is not None and srctype == 'json':
#                    print 'dict w/ image name'
#                    pluginData = pluginImages
#
#                else:
#                    print "no such data key %s" % imageName
#                    abort(404)
#
#            else:
#                pluginImage = pluginImages
#                print "not list"
#
#
#            if pluginImage is None and pluginData is None:
#                print "plugin image is none"
#                abort(404)
#
#            """
#            creates a etag consistent of the fields describing the file and the creation time of the database.
#            with this etag, the browser can cache the images and json files to that the same data is not sent twice.
#            user has to use SHIFT+F5 to overload the cache
#            """
#            etag = "".join([str(x) for x in [dbMtime, projectName, projectStatus, projectSample, sequenceTech, libraryName, fileName, pluginName, pluginKey, imageName]])
#            if pluginImage is not None:
#                """
#                if image, decode
#                returns the decoded PNG image.
#                define the content-length, etag, last-modified and permission to cache for a year.
#                """
#                try:
#                    pluginImageData = base64.b64decode(pluginImage)
#                except:
#                    print "plugin image error converting"
#                    abort(404)
#
#                #response = make_response()
#                #reponse.headers['Cache-Control'] = 'no-cache'
#                #reponse.headers['Content-Type'] = 'image/png'
#                #reponse.headers['Content-Length'] = len(pluginImageData)
#
#                #print "LAST MODIFIED", dbMtime
#                #print "ETAG", etag.replace("/", "").replace("\\", "").replace("_", "").replace(".", "").replace("-", "").replace(" ", "").replace(":", "")
#                #print pluginImageData
#                return Response(pluginImageData,
#                                mimetype="image/png",
#                                headers={
#                                    "Cache-Control" : "public, max-age=36000",
#                                    "Content-Length": len(pluginImageData),
#                                    "ETag"          : etag,
#                                    "Last-Modified" : dbMtime
#                                })
#
#            elif pluginData is not None:
#                """
#                if data, send to the correct graph mapper using the plugin name as key.
#                returns the modified JSON data.
#                define the content-length, etag, last-modified and permission to cache for a year.
#                """
#                qry = (pluginName, pluginKey, imageName)
#                if qry in graph_mapper:
#                    func, func_name, func_nfo = graph_mapper[ qry ]
#                    print "plugin",func_nfo
#                    func_res = func(pluginData, func_name, func_nfo)
#                    return Response(func_res,
#                                    mimetype="application/json",
#                                    headers={
#                                        "Cache-Control" : "public, max-age=36000",
#                                        "Content-Length": len(func_res),
#                                        "ETag"          : etag,
#                                        "Last-Modified" : dbMtime
#                                    })
#
#                else:
#                    print "no data for combination"
#                    abort(404)
#
#    abort(404)
#
#
#@app.route('/fullscreen', methods=['GET'])
#@templated('fullscreen.html')
#def fullscreen():
#    """
#    show images and graphs in full screen replacing the /fullscreen for /download as the
#    download link so that jquery can ask for the correct image
#    """
#    srcType = request.args['srctype']
#
#    dlink   = url_for('download') + request.url[len(request.base_url):]
#    #print dlink
#
#    return { 'downloadLnk':dlink, 'srcType': srcType }
#
#
#@app.route('/favicon.ico')
#def favicon():
#    """
#    sends favicon directly to user
#    """
#    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype="image/vnd.microsoft.icon")
#
#
#@app.context_processor
#def utility_processor():
#    """
#    set of "macros" that can be directly used in the templates
#    """
#
#    """
#    unity/format converter for each column
#    """
#    #TODO: move up
#    converter = {
#        'info': {
#            '_plugin'           : 'Info',
#            'size'              : ['File Size'         , sizeToGb   , summing ],
#            'mtime'             : ['C. Time'           , convTime   , None    ]
#        },
#        'quals': {
#            '_plugin'           : 'Quality',
#            'seqLenSum'         : [ 'Total Size'       , sizeTo     , summing ],
#            'Q30BP'             : [ 'Bp (Q>=30)'       , sizeTo     , summing ],
#            'COV'               : [ 'Coverage'         , sizeTo     , summing ],
#            'adaptamerSum%'     : [ '% w/ Adaptamer'   , perc       , average ],
#            'seqAvgLen'         : [ 'Average Length'   , sizeTo     , average ],
#            'flx%'              : [ '% FLX'            , perc       , average ],
#            'Ns%'               : [ '% Ns'             , perc       , average ],
#            'xlr%'              : [ '% XLR'            , perc       , average ],
#            'sumRealFileSize'   : [ 'Decomp. File Size', sizeToGb   , summing ],
#            'Q30COV'            : [ 'Cov. (Q>=30)'     , roundToTwo , summing ],
#            'Q30'               : [ '% Q>=30'          , roundToTwo , average ],
#            'numSeqs'           : [ '# Seq.'           , sizeTo     , summing ],
#            'formatType'        : [ 'Format'           , None       , None    ]
#        },
#        'fastqc': {
#            '_plugin'           : 'FastQC',
#            'fastqcGraphs'      : ['FastQC Graphs'     , parseGraph , returnE ],
#        },
#        'contamination': {
#            '_plugin'           : 'Contamination',
#            #'contaminationGraph': ['Graph'             , parseGraph , None    ]
#            'contaminationData' : ['Graph'             , parseGraph , None    ]
#        }
#    }
#
#    statistics = stat(converter)
#    """
#    initializes the statistics class to calculate averages and sums by colum
#    """
#
#    def cleanName(filename):
#        """
#        clean raw files file names
#        """
#        #print "FILE NAME",filename
#        filename = os.path.basename(filename)
#
#        for replaceable in REPLACEABLES:
#            filename = filename.replace(replaceable, REPLACEABLES[replaceable])
#
#        return filename
#
#    def checkPlugin(pluginName):
#        """
#        plugins to be skipped altogether
#        """
#        return pluginName not in SKIPPLUGINS
#
#    def checkPluginKey(pluginName, pluginKey):
#        """
#        keys to be skipped
#        """
#        if pluginName in SKIPKEYS:
#            if pluginKey in SKIPKEYS[pluginName]:
#                return False
#
#        return True
#
#    def converterPlugin(pluginName):
#        """
#        check if should be converted or not
#        """
#        if pluginName in converter:
#            if '_plugin' in converter[pluginName]:
#                return converter[pluginName]['_plugin']
#
#        return pluginName
#
#    def converterKey(pluginName, key):
#        """
#        checks if key shoudl be converted or not
#        """
#        if pluginName in converter:
#            if key in converter[pluginName]:
#                conv = converter[pluginName][key][0]
#                if conv is not None:
#                    return conv
#
#        return key
#
#    def converterValue(projectName, projectStatus, projectSample, sequenceTech, libraryName, fileName, pluginName, pluginKey, pluginValue):
#        """
#        checks if value shoud be converted or not. if so, return the converted value
#        """
#        if pluginValue is None:
#            return ""
#
#        if pluginValue == "":
#            return ""
#
#        if pluginName in converter:
#            if pluginKey in converter[pluginName]:
#                conv = converter[pluginName][pluginKey][1]
#                if conv is not None:
#                    res = conv(projectName, projectStatus, projectSample, sequenceTech, libraryName, fileName, pluginName, pluginKey, pluginValue)
#                    if res is None:
#                        return ""
#                    return res
#
#        return pluginValue
#
#
#
#
#    def parseSetup(data):
#        """
#        clean setup and convert it to html
#        """
#        dataf   = {}
#
#        for key in data:
#            if key in SKIPSETUP: continue
#            dataf[key] = data[key]
#
#        return printRaw(dataf)
#        #return syntaxHighlight(dataf)
#
#    def syntaxHighlight(data):
#        """
#        highlight JSON for pretty viewing in HTML
#        """
#        def json2html(match):
#            """
#            checks the data type and add a SPAN around the value with a descriptive class with a color defined by CSS
#            """
#            #print "MATCH",match
#            K = match.group(1)
#            K = K.strip()
#            #print " K '" + K + "'",
#
#            cls = 'jsonnumber'
#
#            if K[0] == '"':
#                if K[-1] == ":":
#                    cls = 'jsonkey'
#                else:
#                    cls = 'jsonstring'
#
#            elif K in ('true', 'false'):
#                cls = 'jsonboolean'
#
#            elif K == 'null':
#                cls = 'jsonnull'
#
#            #print "  CLS",cls
#            return '<span class="%s">%s</span>' % (cls, K)
#
#        json    = jsonpickle.encode( data )
#        json.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;');
#        rep     = r'("(\\u[a-zA-Z0-9]{4}|\\[^u]|[^\\"])*"(\s*:)?|(?:\b|\s)(true|false|null)(?:\b|\s|,)|-?\d+(?:\.\d*)?(?:[eE][+\-]?\d+)?)'
#        repc    = re.compile(rep)
#        jsonRes = repc.sub(json2html, json)
#        #print json
#        #print jsonRes
#        return jsonRes
#
#    def printRaw(data):
#        """
#        print a data structure as nested tabkes
#        """
#        def parseEl(el, level=0, par=""):
#            """
#            recursive function that checks if DICT, LIST or PRIMITIVE and net them accordingly.
#            darkens the background when nesting and adds classes to identify them
#            """
#            col = hex( 255-((255/4)*level) )[2:]
#
#            if isinstance(el, list):
#                res = []
#                #TODO: CONVERT TO MULTI SELECT
#                #res.append('<td class="config fieldlst">')
#
#                for elNum in range(len(el)):
#                    ele = el[elNum]
#                    res.extend( parseEl(ele, level=level+1, par=par+"|"+str(elNum) ) )
#
#                #res.append('</td>')
#
#                return res
#
#            elif isinstance(el, dict):
#                res = []
#
#                if level != 0:
#                    res.append('<td class="config fielddict">')
#
#                res.append("<table>")
#                res.append("<tbody>")
#
#                for key in el:
#                    res.append('<tr bgcolor="#%s%s%s">' % ( col, col, col ))
#                    res.append("<td><b>%s</b></td>" % key)
#                    res.extend( parseEl( el[key], level=level+1, par=par+"|"+key ) )
#                    res.append("</tr>")
#
#                res.append("</tbody>")
#                res.append("</table>")
#
#                if level != 0:
#                    res.append('</td>')
#
#                return res
#
#            else:
#                res = []
#
#                if   isinstance(el, bool ):
#                    res.append('<td class="config fieldbool"  par="%s">%s</td>' % ( par, str(el) ))
#                elif isinstance(el, str  ):
#                    res.append('<td class="config fieldstr"   par="%s">%s</td>' % ( par, str(el) ))
#                elif isinstance(el, int  ):
#                    res.append('<td class="config fieldint"   par="%s">%s</td>' % ( par, str(el) ))
#                elif isinstance(el, float):
#                    res.append('<td class="config fieldfloat" par="%s">%s</td>' % ( par, str(el) ))
#                else:
#                    res.append('<td class="config fieldunk"   par="%s">%s</td>' % ( par, str(el) ))
#
#                return res
#
#        res = parseEl( data )
#
#
#
#        #TODO: print only the data concerning the current request
#        res.append("<table>")
#        res.append("<thead>")
#        lcount = 0
#        for line in g.projectDescription:
#            if lcount == 0 and line[0][0] == "#":
#                line[0] = line[0][1:]
#
#            res.append("<tr>")
#
#            for row in line:
#                if lcount == 0:
#                    res.append("<th>%s</th>" % row.replace('_', " ").capitalize())
#
#                else:
#                    res.append("<td>%s</td>" % row)
#
#            res.append("</tr>")
#
#            if lcount == 0:
#                res.append("</thead>")
#                res.append("<tbody>")
#
#            lcount += 1
#        res.append("</tbody>")
#        res.append("</table>")
#
#        return "\n".join(res)
#
#
#
#
#    def length(var):
#        """
#        returns the length of a variable
#        """
#        return len(var)
#
#    def stats(**kwargs):
#        """
#        calculates the statistics for a given set
#        """
#        s = statistics.add(**kwargs)
#        if s is None:
#            return ""
#
#        return s
#
#    return dict(cleanName       = cleanName,
#                checkPlugin     = checkPlugin,
#                checkPluginKey  = checkPluginKey,
#                converterPlugin = converterPlugin,
#                converterKey    = converterKey,
#                converterValue  = converterValue,
#                parseSetup      = parseSetup,
#                length          = length,
#                stats           = stats
#                )
#
#
#
##DATABASE
#def init_db():
#    """
#    reads the data from the disk, parses and loads it to global variables.
#    has to be changed if using WSGI servers aroung it (eg. apache) once global variables
#    are not shared.
#    """
#    with app.app_context():
#        print "initializing db"
#
#        if not os.path.exists(setupDBFile):
#            print "NO SETUP DATABASE (DB) FILE %s" % setupDBFile
#            sys.exit(1)
#
#        if not os.path.exists(structureFile):
#            print "NO STRUCTURE FILE %s" % structureFile
#            sys.exit(1)
#
#        if not os.path.exists(projectDescriptionFile):
#            print "NO PROJECT DESCRIPTION FILE %s" % projectDescriptionFile
#            sys.exit(1)
#
#        global setupDB
#        global projects
#        global structure
#        global dbMtime
#        global projectDescription
#
#        dbMtime = os.stat(structureFile).st_mtime
#        dbMtime = time.ctime(dbMtime)
#
#        jsonpickle.set_preferred_backend('simplejson')
#        jsonpickle.set_encoder_options('simplejson', sort_keys=True, indent=1)
#
#        setupDB   = jsonpickle.decode(open(setupDBFile,   'r').read())
#        structure = jsonpickle.decode(open(structureFile, 'r').read())
#
#        #folders     =   [
#        #            #root                          name            type               subs       libs             to be cleaned
#        #            [os.path.join(base ,"denovo"), "arcanum"     , constants.DENOVO , None     , denovoLibs     , True ],
#        #        ]
#
#        """
#        reads project description CSV file
#        """
#        projectDescription = []
#        with open(projectDescriptionFile, 'r') as pdf:
#            for line in pdf:
#                #if line[0] == '#': continue
#                data = line.split("\t")
#                projectDescription.append( data )
#
#
#
#        """
#        reads project
#        """
#        projects = {}
#        for proj in setupDB['folders']:
#            projname = proj[1]
#            projects[ projname ] = {
#                "root"   : proj[0],
#                "name"   : projname,
#                "type"   : setupDB['constants']['types'][proj[2]],
#                "samples": proj[3],
#                "libs"   : {},
#                "toClean": proj[5],
#            }
#
#            #["illumina",    [
#            #        [ "pairedend_170", 'PE',  '170' ],
#            for techd in proj[4]:
#                tname = techd[0]
#                projects[ projname ]["libs"][tname] = {}
#
#                for libd in techd[1]:
#                    lname = libd[0]
#                    ltype = libd[1]
#                    lsize = libd[2]
#
#                    if lsize is None:
#                        lsize = 0
#
#                    projects[ projname ]["libs"][tname][lname] = {
#                            "type": ltype,
#                            "size": lsize,
#                            "name": lname
#                    }
#
#
#
#        if setupDB is None:
#            print "no setupDB data"
#            sys.exit(1)
#
#        if structure is None:
#            print "no structure data"
#            sys.exit(1)
#
#
#
#        global projectStatuses
#        global plugins
#        projectStatuses = []
#        plugins         = {}
#        stop            = False
#
#        """
#        loads plugins and statuses variables
#        """
#        for projectName in structure:
#            projStatuses = structure[projectName]
#            projectBase  = os.path.join(setup.getProjectRoot(projectName), projectName)
#            if stop: break
#            for projectStatus in projStatuses:
#                if projectStatus not in projectStatuses: projectStatuses.append(projectStatus)
#                samples     = structure[projectName][projectStatus]
#                if stop: break
#                for projectSample in samples:
#                     if projectSample != None:
#                        technologies     = samples[projectSample]
#                        if stop: break
#                        for sequenceTech in technologies:
#                            if sequenceTech != None:
#                                libs     = technologies[sequenceTech]
#                                if stop: break
#                                for libraryName in libs:
#                                    if libraryName != None:
#                                        fileNames     = libs[libraryName]
#                                        if stop: break
#                                        for fileName in fileNames:
#                                            if fileName != None:
#                                                data     = fileNames[fileName]
#                                                pairName = data.pairName
#                                                for pluginName in data.getPlugins():
#                                                    if pluginName not in plugins:
#                                                        plugins[pluginName] = []
#
#                                                    if pluginName not in []:
#                                                        pluginData = data.getPlugin(pluginName)
#                                                        for pluginKey in pluginData:
#
#                                                            if pluginKey == 'parent':
#                                                                continue
#
#                                                            if pluginKey not in plugins[pluginName]:
#                                                                plugins[pluginName].append(pluginKey)
#
#                                                            #TODO: do i still need to get the value?
#                                                            #('fastqc', 'fastqcGraphs'), ('contamination', 'contaminationGraph')
#                                                            if (pluginName, pluginKey) not in [('info', 'ident'), ('info', 'parent'), ('quals', 'data') ]:
#                                                                val = data.getPluginResult(pluginName, pluginKey)
#
#                                                                #if pluginKey == 'fastqcGraphs':
#                                                                #    for key in val:
#                                                                #        plugins[pluginName].append(key)
#                                                stop = True
#                                                break
#
#        projectStatuses.sort()
#
#        print "db loaded"
#
#
#def getDb():
#    """
#    if db has not been initialized yet, do it so. Otherwise, just return the global variables
#    """
#    if setupDB is None:
#        init_db()
#
#    return [setupDB, projects, structure, projectDescription, projectStatuses, plugins]


