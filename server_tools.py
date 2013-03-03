import time


def sizeToGb(*args):
    """
    convert from bytes do SI human readable
    """
    size = args[-1]

    if size is None:
        return "None"

    try:
        float(size)
    except TypeError:
        print "COULD NOT CONVERT TO FLOAT", size
        raise


    if size <= 1024:
        return "%.3f bytes" % size

    size = float(size) / 1024
    if size <= 1024:
        return "%.3f Kb"  % size

    size = float(size) / 1024
    if size <= 1024:
        return "%.3f Mb"  % size

    size = float(size) / 1024
    if size <= 1024:
        return "%.3f Gb"  % size

    size = float(size) / 1024
    return "%.3f Tb"  % size

def sizeTo(*args):
    """
    convert from number to formated rounded number
    """
    size = args[-1]

    if size is None:
        return "None"

    try:
        float(size)
    except TypeError:
        print "COULD NOT CONVERT TO FLOAT", size
        raise

    if size <= 1000:
        return "%.3f"  % size

    size = float(size) / 1000
    if size <= 1000:
        return "%.3f K"  % size

    size = float(size) / 1000
    if size <= 1000:
        return "%.3f Mi"  % size

    size = float(size) / 1000
    if size <= 1000:
        return "%.3f Bi"  % size

    size = float(size) / 1000
    return "%.3f Tr"  % size

def perc(*args):
    """
    return rounded float string appended with a %
    """
    value = args[-1]

    if value is None:
        return "None"

    try:
        float(value)
    except TypeError:
        print "COULD NOT CONVERT TO FLOAT", value
        raise

    return '%.2f%%' % value

def roundToTwo(*args):
    """
    return a rounded float string
    """
    value = args[-1]

    if value is None:
        return "None"

    try:
        float(value)
    except TypeError:
        print "COULD NOT CONVERT TO FLOAT", value
        raise

    fmt = "%.2f"
    return fmt % value

def convTime(*args):
    """
    convert time from ctime to literal time
    """
    value = args[-1]

    if value is None:
        return "None"

    try:
        float(value)
    except TypeError:
        #print "COULD NOT CONVERT TYPE TO FLOAT", value
        return ""
    except ValueError:
        #print "COULD NOT CONVERT VALUE TO FLOAT", value
        return ""

    return time.ctime(value)





class summing(object):
    """
    class to keep track of sums
    """
    def __init__(self):
        self.val = 0

    def add(self, val):
        #print "summing",val
        self.val += val

    def get(self):
        #print "summing returning",self.val
        return self.val

class average(object):
    """
    class to generate average
    """
    def __init__(self):
        self.val   = 0
        self.count = 0

    def add(self, val):
        self.val   += val
        self.count += 1

    def get(self):
        if self.count == 0:
            return -1
        if self.val == 0:
            return 0

        return float(self.val) / self.count

class returnE(object):
    """
    class to return empty value
    """
    def add(self, val):
        pass

    def get(self):
        return {}



class stat(object):
    """
    class to keep track of statistics for each branch in the data tree
    """
    def __init__(self, translator):
        self.data       = {}
        self.translator = translator

    def add(self, **kwargs):
        convert = None
        if 'plugin' in kwargs:
            plugin = kwargs['plugin']

            if 'key' in kwargs:
                key     = kwargs['key'   ]
                convert = self.translator[plugin][key][2]
                if convert is not None:
                    convert = convert

            else:
                return None
        else:
            return None


        if 'name' in kwargs:
            name = kwargs['name']

            if plugin not in self.data:
                self.data[plugin] = {}

            if key not in self.data[plugin]:
                self.data[plugin][key] = {}

            if name not in self.data[plugin][key]:
                try   : conv = convert()
                except: conv = None
                self.data[plugin][key][name] = { 'stat': conv, 'status': {} }

            if 'status' in kwargs:
                status = kwargs['status']
                if status not in self.data[plugin][key][name]['status']:
                    try   : conv = convert()
                    except: conv = None
                    self.data[plugin][key][name]['status'][status] = { 'stat': conv, 'samples': {} }

                if 'sample' in kwargs:
                    sample = kwargs['sample']
                    if sample not in self.data[plugin][key][name]['status'][status]['samples']:
                        try   : conv = convert()
                        except: conv = None
                        self.data[plugin][key][name]['status'][status]['samples'][sample] = { 'stat': conv, 'techs': {} }

                    if 'tech' in kwargs:
                        tech = kwargs['tech']
                        if tech not in self.data[plugin][key][name]['status'][status]['samples'][sample]['techs']:
                            try   : conv = convert()
                            except: conv = None
                            self.data[plugin][key][name]['status'][status]['samples'][sample]['techs'][tech] = { 'stat': conv, 'libs': {} }

                        if 'lib' in kwargs:
                            lib = kwargs['lib']
                            if lib not in self.data[plugin][key][name]['status'][status]['samples'][sample]['techs'][tech]['libs']:
                                try   : conv = convert()
                                except: conv = None
                                self.data[plugin][key][name]['status'][status]['samples'][sample]['techs'][tech]['libs'][lib] = { 'stat': conv, 'plugins': {} }

                            if 'value' in kwargs:
                                value = kwargs['value']
                                try   : self.data[plugin][key][name]['status'][status]['samples'][sample]['techs'][tech]['libs'][lib]['stat'].add(value)
                                except: pass

                                try   : self.data[plugin][key][name]['status'][status]['samples'][sample]['techs'][tech]['stat'].add(value)
                                except: pass

                                try   : self.data[plugin][key][name]['status'][status]['samples'][sample]['stat'].add(value)
                                except: pass

                                try   : self.data[plugin][key][name]['status'][status]['stat'].add(value)
                                except: pass

                                try   : self.data[plugin][key][name]['stat'].add(value)
                                except: pass

                            else: # lib
                                try   : res = self.data[plugin][key][name]['status'][status]['samples'][sample]['techs'][tech]['libs'][lib]['stat'].get()
                                except: res = None
                                return res
                        else: # tech
                            try   : res = self.data[plugin][key][name]['status'][status]['samples'][sample]['techs'][tech]['stat'].get()
                            except: res = None
                            return res
                    else: # sample
                        try   : res = self.data[plugin][key][name]['status'][status]['samples'][sample]['stat'].get()
                        except: res = None
                        return res
                else: # status
                    try   : res = self.data[plugin][key][name]['status'][status]['stat'].get()
                    except: res = None
                    return res
            else: # name
                try   : res = self.data[plugin][key][name]['stat'].get()
                except: res = None
                return res
        else:
            return None
