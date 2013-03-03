



#{% macro render_field( field ) %}
#    <dt>{{ field.name }}</dt>
#    <dd>{{ field(**kwargs)|safe }}
#        {% if field.errors %}
#            <ul class=errors>
#                {% for error in field.error %}
#                    <li> {{ errror }} </li>
#                {% endfor %}
#            </ul>
#        {% endif %}
#    </dd>
#{% endmacro %}
#
#
#<form method=post action="/configure">
#    <dl>
#        {% for field in g.formtoreq %}
#            {{ render_field(field) }}
#        {% endfor %}
#    </dl>
#</form>

#from flask.ext.wtf import Form, SubmitField, BooleanField, FormField, FieldList, TextField, TextAreaField, IntegerField, validators, SelectMultipleField, Required
#
#class subProjectDescription(Form):
#    baseFolder = TextField("baseFolder")
#    name       = TextField("name")
#    projtype   = IntegerField("project type")
#    folders    = TextAreaField()
#    methodol   = TextField("name")
#
#
#class setupForm(Form):
#    submit           = SubmitField("Submit")
#    # BEHAVIOR
#    DoAdaptamers     = BooleanField("Clean 454 Adaptamers?", description="For the 454 data, should the adaptamers be cleaned?")
#    Qborder          = IntegerField("Trim at Q="           , description="which Q value to trim files")
#    projectsToIgnore = SelectMultipleField("Projects to Ignore", [])
#
#    projectsToIgnore.choices = [("reseq", "reseq")]
#
#    # PROGRAMS
#    baseFolder   = TextField(   "Base Folder", [validators.Length(min=1, max=256), validators.Required()], description="Base folder for all analysis")
#    dbFile       = TextField(   "Cleaning DB", [validators.Length(min=1, max=256), validators.Required()], description="Database for cleaning")
#
#    proj         = FormField(subProjectDescription)
#    #FILES




# "base": "/home/assembly/tomato150",
#  "types": [
#   "DENOVO",
#   "MAPPING"
#  ]
# },
# "contamClean": {
#  "454": {
#   "db": "/home/assembly/tomato150/scripts/pipeline/progs/contam/db/contamination_without_ecolidb_v0.2.fa",
#   "threshold": 85
#  },
#  "illumina": {
#   "db": "/home/assembly/tomato150/scripts/pipeline/progs/contam/db/contamination_without_ecolidb_v0.2.fa",
#   "threshold": 95
#  }
# },
# "currAbsPath": "",
# "currFtpPath": "/home/assembly/tomato150/scripts/ftp",
# "debug":false,

# "does": {
#  "contamination":true,
#  "fastqc":true,
#  "hash":true,
#  "quals":true
# },
# "dscFileName": "/home/assembly/tomato150/project_description.csv",
# "exportToFile":true,
# "filter454": {
#  "compressHomopolymerSize": 1,
#  "filterDuplicates": 1,
#  "maxCompressedSize": 850,
#  "maxNs": 1,
#  "minCompressedSize": 50,
#  "seedLength": 50,
#  "trim5": 0.1
# },
# "folder": [
#  "/home/assembly/tomato150",
#  "reseq",
#  1,
#  [
#   "001",
#   "002",
#   "003",
#   "004",
#   "005",
#   "006",
#   "007",
#   "008",
#   "011",
#   "012",
#   "013",
#   "014",
#   "015",
#   "016",
#   "017",
#   "018",
#   "019",
#   "020",
#   "021",
#   "022",
#   "023",
#   "024",
#   "026",
#   "027",
#   "028",
#   "029",
#   "030",
#   "031",
#   "032",
#   "033",
#   "034",
#   "035",
#   "036",
#   "037",
#   "038",
#   "039",
#   "040",
#   "041",
#   "077",
#   "078",
#   "088",
#   "089",
#   "090",
#   "091",
#   "093",
#   "094",
#   "096",
#   "097",
#   "102",
#   "103",
#   "105",
#   "025",
#   "042",
#   "043",
#   "044",
#   "045",
#   "046",
#   "047",
#   "049",
#   "051",
#   "052",
#   "053",
#   "054",
#   "055",
#   "056",
#   "057",
#   "058",
#   "059",
#   "060",
#   "062",
#   "063",
#   "064",
#   "065",
#   "066",
#   "067",
#   "068",
#   "069",
#   "070",
#   "071",
#   "072",
#   "073",
#   "074",
#   "075",
#   "104naturalis_Moneymaker-CF4N705",
#   "naturalis_Moneymaker-CF4N706",
#   "naturalis_Moneymaker-oldN703",
#   "naturalis_Moneymaker-oldN704",
#   "naturalis_Slyc-17N701",
#   "naturalis_Slyc-17N702"
#  ],
#  [
#   [
#    "illumina",
#    [
#     [
#      "pairedend_500",
#      "PE",
#      "500"
#     ]
#    ]
#   ]
#  ],
# false,
#  [
#   "docs",
#   "_prelim",
#   "_prefiltered",
#   "raw",
#   "filtered",
#   "_tmp",
#   "mapped"
#  ]
# ],
# "folderType": 1,
# "folders": [
#  [
#   "/home/assembly/tomato150/denovo",
#   "arcanum",
#   0,
#  null,
#   [
#    [
#     "illumina",
#     [
#      [
#       "pairedend_170",
#       "PE",
#       "170"
#      ],
#      [
#       "matepair_2000",
#       "MP",
#       "2000"
#      ]
#     ]
#    ],
#    [
#     "454",
#     [
#      [
#       "8000",
#       "MP",
#       "8000"
#      ],
#      [
#       "20000",
#       "MP",
#       "20000"
#      ],
#      [
#       "shotgun",
#       "WGS",
#      null
#      ]
#     ]
#    ]
#   ],
#  true,
#   [
#    "docs",
#    "_prelim",
#    "_prefiltered",
#    "raw",
#    "filtered",
#    "_tmp",
#    "assembled"
#   ]
#  ],
#  [
#   "/home/assembly/tomato150/denovo",
#   "habrochaites",
#   0,
#  null,
#   [
#    [
#     "illumina",
#     [
#      [
#       "pairedend_170",
#       "PE",
#       "170"
#      ],
#      [
#       "matepair_2000",
#       "MP",
#       "2000"
#      ]
#     ]
#    ],
#    [
#     "454",
#     [
#      [
#       "8000",
#       "MP",
#       "8000"
#      ],
#      [
#       "20000",
#       "MP",
#       "20000"
#      ],
#      [
#       "shotgun",
#       "WGS",
#      null
#      ]
#     ]
#    ]
#   ],
#  true,
#   [
#    "docs",
#    "_prelim",
#    "_prefiltered",
#    "raw",
#    "filtered",
#    "_tmp",
#    "assembled"
#   ]
#  ],
#  [
#   "/home/assembly/tomato150/denovo",
#   "pennellii",
#   0,
#  null,
#   [
#    [
#     "illumina",
#     [
#      [
#       "pairedend_170",
#       "PE",
#       "170"
#      ],
#      [
#       "matepair_2000",
#       "MP",
#       "2000"
#      ]
#     ]
#    ],
#    [
#     "454",
#     [
#      [
#       "8000",
#       "MP",
#       "8000"
#      ],
#      [
#       "20000",
#       "MP",
#       "20000"
#      ],
#      [
#       "shotgun",
#       "WGS",
#      null
#      ],
#      [
#       "3000",
#       "MP",
#       "3000"
#      ]
#     ]
#    ]
#   ],
#  true,
#   [
#    "docs",
#    "_prelim",
#    "_prefiltered",
#    "raw",
#    "filtered",
#    "_tmp",
#    "assembled"
#   ]
#  ],
#  [
#   "/home/assembly/tomato150",
#   "ril",
#   1,
#   [
#    "601",
#    "603",
#    "608",
#    "609",
#    "610",
#    "611",
#    "612",
#    "614",
#    "615",
#    "618",
#    "619",
#    "622",
#    "623",
#    "624",
#    "625",
#    "626",
#    "630",
#    "631",
#    "634",
#    "639",
#    "643",
#    "644",
#    "646",
#    "648",
#    "649",
#    "651",
#    "653",
#    "654",
#    "656",
#    "658",
#    "659",
#    "660",
#    "665",
#    "666",
#    "667",
#    "668",
#    "669",
#    "670",
#    "674",
#    "675",
#    "676",
#    "678",
#    "679",
#    "682",
#    "684",
#    "685",
#    "688",
#    "691",
#    "692",
#    "693",
#    "694",
#    "696",
#    "697",
#    "701",
#    "702",
#    "705",
#    "706",
#    "707",
#    "710",
#    "711"
#   ],
#   [
#    [
#     "illumina",
#     [
#      [
#       "pairedend_500",
#       "PE",
#       "500"
#      ]
#     ]
#    ]
#   ],
#  true,
#   [
#    "docs",
#    "_prelim",
#    "_prefiltered",
#    "raw",
#    "filtered",
#    "_tmp",
#    "mapped"
#   ]
#  ],
#  [
#   "/home/assembly/tomato150",
#   "reseq",
#   1,
#   [
#    "001",
#    "002",
#    "003",
#    "004",
#    "005",
#    "006",
#    "007",
#    "008",
#    "011",
#    "012",
#    "013",
#    "014",
#    "015",
#    "016",
#    "017",
#    "018",
#    "019",
#    "020",
#    "021",
#    "022",
#    "023",
#    "024",
#    "026",
#    "027",
#    "028",
#    "029",
#    "030",
#    "031",
#    "032",
#    "033",
#    "034",
#    "035",
#    "036",
#    "037",
#    "038",
#    "039",
#    "040",
#    "041",
#    "077",
#    "078",
#    "088",
#    "089",
#    "090",
#    "091",
#    "093",
#    "094",
#    "096",
#    "097",
#    "102",
#    "103",
#    "105",
#    "025",
#    "042",
#    "043",
#    "044",
#    "045",
#    "046",
#    "047",
#    "049",
#    "051",
#    "052",
#    "053",
#    "054",
#    "055",
#    "056",
#    "057",
#    "058",
#    "059",
#    "060",
#    "062",
#    "063",
#    "064",
#    "065",
#    "066",
#    "067",
#    "068",
#    "069",
#    "070",
#    "071",
#    "072",
#    "073",
#    "074",
#    "075",
#    "104naturalis_Moneymaker-CF4N705",
#    "naturalis_Moneymaker-CF4N706",
#    "naturalis_Moneymaker-oldN703",
#    "naturalis_Moneymaker-oldN704",
#    "naturalis_Slyc-17N701",
#    "naturalis_Slyc-17N702"
#   ],
#   [
#    [
#     "illumina",
#     [
#      [
#       "pairedend_500",
#       "PE",
#       "500"
#      ]
#     ]
#    ]
#   ],
#  false,
#   [
#    "docs",
#    "_prelim",
#    "_prefiltered",
#    "raw",
#    "filtered",
#    "_tmp",
#    "mapped"
#   ]
#  ]
# ],
# "genomeSize": 950000000,
# "ignoreDb":false,
# "jellyfishParams": {
#  "_extra": "--both-strands",
#  "counter-len": 7,
#  "high": 300,
#  "increment": 1,
#  "low": 1,
#  "lower-count": 1,
#  "mer-len": 19,
#  "out-buffer-size": 800000000,
#  "out-counter-len": 4,
#  "size": 800000000,
#  "threads": 8
# },
# "key": "quakecutoff",
# "loadLocalDbs":true,
# "mappingLibs": [
#  [
#   "illumina",
#   [
#    [
#     "pairedend_500",
#     "PE",
#     "500"
#    ]
#   ]
#  ]
# ],
# "maxThreads": 1,
# "mergePdfs":true,
# "nameLength": 12,
# "projLength": 6,

# "quakeParams": {
#  "--no_cut":false,
#  "--ratio": 800,
#  "-p": 10
# },
# "quakecutoff": {
#  "arcanum": 4,
#  "habrochaites": 4,
#  "pennellii": 4
# },
# "quakeignore": [
#  "ril",
#  "reseq"
# ],
# "redo": {
#  "compression":false,
#  "contamination":false,
#  "fastqc":false,
#  "hash":false,
#  "info":false,
#  "quals":false
# },
# "redoReport":false,
# "replaceFiles":true,
# "reseqSubs": [
#  "001",
#  "002",
#  "003",
#  "004",
#  "005",
#  "006",
#  "007",
#  "008",
#  "011",
#  "012",
#  "013",
#  "014",
#  "015",
#  "016",
#  "017",
#  "018",
#  "019",
#  "020",
#  "021",
#  "022",
#  "023",
#  "024",
#  "026",
#  "027",
#  "028",
#  "029",
#  "030",
#  "031",
#  "032",
#  "033",
#  "034",
#  "035",
#  "036",
#  "037",
#  "038",
#  "039",
#  "040",
#  "041",
#  "077",
#  "078",
#  "088",
#  "089",
#  "090",
#  "091",
#  "093",
#  "094",
#  "096",
#  "097",
#  "102",
#  "103",
#  "105",
#  "025",
#  "042",
#  "043",
#  "044",
#  "045",
#  "046",
#  "047",
#  "049",
#  "051",
#  "052",
#  "053",
#  "054",
#  "055",
#  "056",
#  "057",
#  "058",
#  "059",
#  "060",
#  "062",
#  "063",
#  "064",
#  "065",
#  "066",
#  "067",
#  "068",
#  "069",
#  "070",
#  "071",
#  "072",
#  "073",
#  "074",
#  "075",
#  "104naturalis_Moneymaker-CF4N705",
#  "naturalis_Moneymaker-CF4N706",
#  "naturalis_Moneymaker-oldN703",
#  "naturalis_Moneymaker-oldN704",
#  "naturalis_Slyc-17N701",
#  "naturalis_Slyc-17N702"
# ],
# "rilSubs": [
#  "601",
#  "603",
#  "608",
#  "609",
#  "610",
#  "611",
#  "612",
#  "614",
#  "615",
#  "618",
#  "619",
#  "622",
#  "623",
#  "624",
#  "625",
#  "626",
#  "630",
#  "631",
#  "634",
#  "639",
#  "643",
#  "644",
#  "646",
#  "648",
#  "649",
#  "651",
#  "653",
#  "654",
#  "656",
#  "658",
#  "659",
#  "660",
#  "665",
#  "666",
#  "667",
#  "668",
#  "669",
#  "670",
#  "674",
#  "675",
#  "676",
#  "678",
#  "679",
#  "682",
#  "684",
#  "685",
#  "688",
#  "691",
#  "692",
#  "693",
#  "694",
#  "696",
#  "697",
#  "701",
#  "702",
#  "705",
#  "706",
#  "707",
#  "710",
#  "711"
# ],
# "runFastqc":false,
# "runGenData":true,
# "runJellyfish":true,
# "runQuake":true,
# "runSolexaqa":false,
# "samplesToIgnore": [],
# "skip454":false,
# "skipIllumina":false,
# "sleepWhileWaiting": 10,
# "startTime": "20121215021329",
# "status": [
#  "filtered",
#  "FILTERED",
#  "docs",
#  "filtered"
# ],











#  "programs": {
#   "dymTrim": {
#    "exeDynamicTrim": "perl /mnt/nexenta/assembly/nobackup/dev_150/scripts/pipeline/progs/solexaqa/DynamicTrim.pl",
#    "exeLengthSort": "perl /mnt/nexenta/assembly/nobackup/dev_150/scripts/pipeline/progs/solexaqa/LengthSort.pl",
#    "tmp": "/mnt/nexenta/assembly/nobackup/tmp"
#   },
#   "fastqCount": {
#    "exe": "/home/aflit001/bin/fastqCount",
#    "tmp": "/run/shm"
#   },
#   "fastqScreen": {
#    "exe": "fastq_screen",
#    "subset": 5000,
#    "threads": 8
#   },
#   "fastqc": {
#    "exe": "perl /home/assembly/tomato150/scripts/pipeline/progs/FastQC/fastqc",
#    "threads": 4
#   },
#   "filter454": {
#    "exeAnalyze": "python /mnt/nexenta/assembly/nobackup/dev_150/scripts/pipeline/progs/filter454/analyze454Reads.py",
#    "exeFilter": "python /mnt/nexenta/assembly/nobackup/dev_150/scripts/pipeline/progs/filter454/filter454Reads.py",
#    "exeFq2Fa": "/home/assembly/bin/fastq_to_fasta",
#    "exeSffFile": "/opt/454/2.6_1/bin/sfffile",
#    "exeSffInfo": "/opt/454/2.6_1/bin/sffinfo",
#    "tmp": "/run/shm"
#   },
#   "jellyfish": {
#    "exe": "jellyfish",
#    "pv": " | pv --buffer-size 16M -q ",
#    "tmp": "/run/shm"
#   },
#   "mkplot": {
#    "miY": 3,
#    "q": 80
#   },
#   "quake": {
#    "exe": "python progs/Quake/bin/quake.py",
#    "tmp": "/home/assembly/tmp"
#   },
#   "sffExtract": {
#    "exeFastaAndQualMerge": "python /home/assembly/tomato150/scripts/pipeline/progs/fastqmergefastaandqual.py",
#    "exeSffFile": "/opt/454/2.6_1/bin/sfffile",
#    "exeSffInfo": "/opt/454/2.6_1/bin/sffinfo"
#   },
#   "solexaqa": {
#    "exe": "perl /home/assembly/tomato150/scripts/pipeline/progs/solexaqa/SolexaQA.pl"
#   },
#   "zip": {
#    "exe": "pigz"
#   }
#  },
#  "pv": " | pv --buffer-size 16M -q ",
#  "sffExt": [
#   "/opt/454/2.6_1/bin/sffinfo -s %(in)s  | pv --buffer-size 16M -q  > %(out)s.fasta",
#   "/opt/454/2.6_1/bin/sffinfo -q %(in)s  | pv --buffer-size 16M -q  > %(out)s.fasta.qual",
#   "python /home/assembly/tomato150/scripts/pipeline/progs/fastqmergefastaandqual.py %(out)s.fasta %(out)s.fasta.qual %(out)s",
#   "rm -f %(out)s.fasta %(out)s.fasta.qual"
#  ],
# "contamClean": {
#  "454": {
#   "db": "/home/assembly/tomato150/scripts/pipeline/progs/contam/db/contamination_without_ecolidb_v0.2.fa",
#   "threshold": 85
#  },
#  "illumina": {
#   "db": "/home/assembly/tomato150/scripts/pipeline/progs/contam/db/contamination_without_ecolidb_v0.2.fa",
#   "threshold": 95
#  }
# },
# "currAbsPath": "",
# "currFtpPath": "/home/assembly/tomato150/scripts/ftp",
# "debug":false,

# "does": {
#  "contamination":true,
#  "fastqc":true,
#  "hash":true,
#  "quals":true
# },
# "dscFileName": "/home/assembly/tomato150/project_description.csv",
# "exportToFile":true,
# "filter454": {
#  "compressHomopolymerSize": 1,
#  "filterDuplicates": 1,
#  "maxCompressedSize": 850,
#  "maxNs": 1,
#  "minCompressedSize": 50,
#  "seedLength": 50,
#  "trim5": 0.1
# },
# "folder": [
#  "/home/assembly/tomato150",
#  "reseq",
#  1,
#  [
#   "001",
#   "002",
#   "003",
#   "004",
#   "005",
#   "006",
#   "007",
#   "008",
#   "011",
#   "012",
#   "013",
#   "014",
#   "015",
#   "016",
#   "017",
#   "018",
#   "019",
#   "020",
#   "021",
#   "022",
#   "023",
#   "024",
#   "026",
#   "027",
#   "028",
#   "029",
#   "030",
#   "031",
#   "032",
#   "033",
#   "034",
#   "035",
#   "036",
#   "037",
#   "038",
#   "039",
#   "040",
#   "041",
#   "077",
#   "078",
#   "088",
#   "089",
#   "090",
#   "091",
#   "093",
#   "094",
#   "096",
#   "097",
#   "102",
#   "103",
#   "105",
#   "025",
#   "042",
#   "043",
#   "044",
#   "045",
#   "046",
#   "047",
#   "049",
#   "051",
#   "052",
#   "053",
#   "054",
#   "055",
#   "056",
#   "057",
#   "058",
#   "059",
#   "060",
#   "062",
#   "063",
#   "064",
#   "065",
#   "066",
#   "067",
#   "068",
#   "069",
#   "070",
#   "071",
#   "072",
#   "073",
#   "074",
#   "075",
#   "104naturalis_Moneymaker-CF4N705",
#   "naturalis_Moneymaker-CF4N706",
#   "naturalis_Moneymaker-oldN703",
#   "naturalis_Moneymaker-oldN704",
#   "naturalis_Slyc-17N701",
#   "naturalis_Slyc-17N702"
#  ],
#  [
#   [
#    "illumina",
#    [
#     [
#      "pairedend_500",
#      "PE",
#      "500"
#     ]
#    ]
#   ]
#  ],
# false,
#  [
#   "docs",
#   "_prelim",
#   "_prefiltered",
#   "raw",
#   "filtered",
#   "_tmp",
#   "mapped"
#  ]
# ],
# "folderType": 1,
# "folders": [
#  [
#   "/home/assembly/tomato150/denovo",
#   "arcanum",
#   0,
#  null,
#   [
#    [
#     "illumina",
#     [
#      [
#       "pairedend_170",
#       "PE",
#       "170"
#      ],
#      [
#       "matepair_2000",
#       "MP",
#       "2000"
#      ]
#     ]
#    ],
#    [
#     "454",
#     [
#      [
#       "8000",
#       "MP",
#       "8000"
#      ],
#      [
#       "20000",
#       "MP",
#       "20000"
#      ],
#      [
#       "shotgun",
#       "WGS",
#      null
#      ]
#     ]
#    ]
#   ],
#  true,
#   [
#    "docs",
#    "_prelim",
#    "_prefiltered",
#    "raw",
#    "filtered",
#    "_tmp",
#    "assembled"
#   ]
#  ],
#  [
#   "/home/assembly/tomato150/denovo",
#   "habrochaites",
#   0,
#  null,
#   [
#    [
#     "illumina",
#     [
#      [
#       "pairedend_170",
#       "PE",
#       "170"
#      ],
#      [
#       "matepair_2000",
#       "MP",
#       "2000"
#      ]
#     ]
#    ],
#    [
#     "454",
#     [
#      [
#       "8000",
#       "MP",
#       "8000"
#      ],
#      [
#       "20000",
#       "MP",
#       "20000"
#      ],
#      [
#       "shotgun",
#       "WGS",
#      null
#      ]
#     ]
#    ]
#   ],
#  true,
#   [
#    "docs",
#    "_prelim",
#    "_prefiltered",
#    "raw",
#    "filtered",
#    "_tmp",
#    "assembled"
#   ]
#  ],
#  [
#   "/home/assembly/tomato150/denovo",
#   "pennellii",
#   0,
#  null,
#   [
#    [
#     "illumina",
#     [
#      [
#       "pairedend_170",
#       "PE",
#       "170"
#      ],
#      [
#       "matepair_2000",
#       "MP",
#       "2000"
#      ]
#     ]
#    ],
#    [
#     "454",
#     [
#      [
#       "8000",
#       "MP",
#       "8000"
#      ],
#      [
#       "20000",
#       "MP",
#       "20000"
#      ],
#      [
#       "shotgun",
#       "WGS",
#      null
#      ],
#      [
#       "3000",
#       "MP",
#       "3000"
#      ]
#     ]
#    ]
#   ],
#  true,
#   [
#    "docs",
#    "_prelim",
#    "_prefiltered",
#    "raw",
#    "filtered",
#    "_tmp",
#    "assembled"
#   ]
#  ],
#  [
#   "/home/assembly/tomato150",
#   "ril",
#   1,
#   [
#    "601",
#    "603",
#    "608",
#    "609",
#    "610",
#    "611",
#    "612",
#    "614",
#    "615",
#    "618",
#    "619",
#    "622",
#    "623",
#    "624",
#    "625",
#    "626",
#    "630",
#    "631",
#    "634",
#    "639",
#    "643",
#    "644",
#    "646",
#    "648",
#    "649",
#    "651",
#    "653",
#    "654",
#    "656",
#    "658",
#    "659",
#    "660",
#    "665",
#    "666",
#    "667",
#    "668",
#    "669",
#    "670",
#    "674",
#    "675",
#    "676",
#    "678",
#    "679",
#    "682",
#    "684",
#    "685",
#    "688",
#    "691",
#    "692",
#    "693",
#    "694",
#    "696",
#    "697",
#    "701",
#    "702",
#    "705",
#    "706",
#    "707",
#    "710",
#    "711"
#   ],
#   [
#    [
#     "illumina",
#     [
#      [
#       "pairedend_500",
#       "PE",
#       "500"
#      ]
#     ]
#    ]
#   ],
#  true,
#   [
#    "docs",
#    "_prelim",
#    "_prefiltered",
#    "raw",
#    "filtered",
#    "_tmp",
#    "mapped"
#   ]
#  ],
#  [
#   "/home/assembly/tomato150",
#   "reseq",
#   1,
#   [
#    "001",
#    "002",
#    "003",
#    "004",
#    "005",
#    "006",
#    "007",
#    "008",
#    "011",
#    "012",
#    "013",
#    "014",
#    "015",
#    "016",
#    "017",
#    "018",
#    "019",
#    "020",
#    "021",
#    "022",
#    "023",
#    "024",
#    "026",
#    "027",
#    "028",
#    "029",
#    "030",
#    "031",
#    "032",
#    "033",
#    "034",
#    "035",
#    "036",
#    "037",
#    "038",
#    "039",
#    "040",
#    "041",
#    "077",
#    "078",
#    "088",
#    "089",
#    "090",
#    "091",
#    "093",
#    "094",
#    "096",
#    "097",
#    "102",
#    "103",
#    "105",
#    "025",
#    "042",
#    "043",
#    "044",
#    "045",
#    "046",
#    "047",
#    "049",
#    "051",
#    "052",
#    "053",
#    "054",
#    "055",
#    "056",
#    "057",
#    "058",
#    "059",
#    "060",
#    "062",
#    "063",
#    "064",
#    "065",
#    "066",
#    "067",
#    "068",
#    "069",
#    "070",
#    "071",
#    "072",
#    "073",
#    "074",
#    "075",
#    "104naturalis_Moneymaker-CF4N705",
#    "naturalis_Moneymaker-CF4N706",
#    "naturalis_Moneymaker-oldN703",
#    "naturalis_Moneymaker-oldN704",
#    "naturalis_Slyc-17N701",
#    "naturalis_Slyc-17N702"
#   ],
#   [
#    [
#     "illumina",
#     [
#      [
#       "pairedend_500",
#       "PE",
#       "500"
#      ]
#     ]
#    ]
#   ],
#  false,
#   [
#    "docs",
#    "_prelim",
#    "_prefiltered",
#    "raw",
#    "filtered",
#    "_tmp",
#    "mapped"
#   ]
#  ]
# ],
# "genomeSize": 950000000,
# "ignoreDb":false,
# "jellyfishParams": {
#  "_extra": "--both-strands",
#  "counter-len": 7,
#  "high": 300,
#  "increment": 1,
#  "low": 1,
#  "lower-count": 1,
#  "mer-len": 19,
#  "out-buffer-size": 800000000,
#  "out-counter-len": 4,
#  "size": 800000000,
#  "threads": 8
# },
# "key": "quakecutoff",
# "loadLocalDbs":true,
# "mappingLibs": [
#  [
#   "illumina",
#   [
#    [
#     "pairedend_500",
#     "PE",
#     "500"
#    ]
#   ]
#  ]
# ],
# "maxThreads": 1,
# "mergePdfs":true,
# "nameLength": 12,
# "projLength": 6,
# "projectsToIgnore": [
#  "reseq"
# ],
# "quakeParams": {
#  "--no_cut":false,
#  "--ratio": 800,
#  "-p": 10
# },
# "quakecutoff": {
#  "arcanum": 4,
#  "habrochaites": 4,
#  "pennellii": 4
# },
# "quakeignore": [
#  "ril",
#  "reseq"
# ],
# "redo": {
#  "compression":false,
#  "contamination":false,
#  "fastqc":false,
#  "hash":false,
#  "info":false,
#  "quals":false
# },
# "redoReport":false,
# "replaceFiles":true,
# "reseqSubs": [
#  "001",
#  "002",
#  "003",
#  "004",
#  "005",
#  "006",
#  "007",
#  "008",
#  "011",
#  "012",
#  "013",
#  "014",
#  "015",
#  "016",
#  "017",
#  "018",
#  "019",
#  "020",
#  "021",
#  "022",
#  "023",
#  "024",
#  "026",
#  "027",
#  "028",
#  "029",
#  "030",
#  "031",
#  "032",
#  "033",
#  "034",
#  "035",
#  "036",
#  "037",
#  "038",
#  "039",
#  "040",
#  "041",
#  "077",
#  "078",
#  "088",
#  "089",
#  "090",
#  "091",
#  "093",
#  "094",
#  "096",
#  "097",
#  "102",
#  "103",
#  "105",
#  "025",
#  "042",
#  "043",
#  "044",
#  "045",
#  "046",
#  "047",
#  "049",
#  "051",
#  "052",
#  "053",
#  "054",
#  "055",
#  "056",
#  "057",
#  "058",
#  "059",
#  "060",
#  "062",
#  "063",
#  "064",
#  "065",
#  "066",
#  "067",
#  "068",
#  "069",
#  "070",
#  "071",
#  "072",
#  "073",
#  "074",
#  "075",
#  "104naturalis_Moneymaker-CF4N705",
#  "naturalis_Moneymaker-CF4N706",
#  "naturalis_Moneymaker-oldN703",
#  "naturalis_Moneymaker-oldN704",
#  "naturalis_Slyc-17N701",
#  "naturalis_Slyc-17N702"
# ],
# "rilSubs": [
#  "601",
#  "603",
#  "608",
#  "609",
#  "610",
#  "611",
#  "612",
#  "614",
#  "615",
#  "618",
#  "619",
#  "622",
#  "623",
#  "624",
#  "625",
#  "626",
#  "630",
#  "631",
#  "634",
#  "639",
#  "643",
#  "644",
#  "646",
#  "648",
#  "649",
#  "651",
#  "653",
#  "654",
#  "656",
#  "658",
#  "659",
#  "660",
#  "665",
#  "666",
#  "667",
#  "668",
#  "669",
#  "670",
#  "674",
#  "675",
#  "676",
#  "678",
#  "679",
#  "682",
#  "684",
#  "685",
#  "688",
#  "691",
#  "692",
#  "693",
#  "694",
#  "696",
#  "697",
#  "701",
#  "702",
#  "705",
#  "706",
#  "707",
#  "710",
#  "711"
# ],
# "runFastqc":false,
# "runGenData":true,
# "runJellyfish":true,
# "runQuake":true,
# "runSolexaqa":false,
# "samplesToIgnore": [],
# "skip454":false,
# "skipIllumina":false,
# "sleepWhileWaiting": 10,
# "startTime": "20121215021329",
# "status": [
#  "filtered",
#  "FILTERED",
#  "docs",
#  "filtered"
# ],
# "statusFolder": "filtered",
# "statuses": [
#  [
#   "_prelim",
#   "PRELIMINARY",
#   "_prelim",
#   "_prelim"
#  ],
#  [
#   "_prefiltered",
#   "PREFILTER",
#   "_prefiltered",
#   "_prefiltered"
#  ],
#  [
#   "raw",
#   "CHECKED",
#   "docs",
#   "raw"
#  ],
#  [
#   "filtered",
#   "FILTERED",
#   "docs",
#   "filtered"
#  ]
# ],
# "statusesToClean": [
#  "CHECKED"
# ],
# "structs": [
#  "docs",
#  "_prelim",
#  "_prefiltered",
#  "raw",
#  "filtered",
#  "_tmp"
# ],
# "tmpFolder": "_tmp",
# "trimFastq": {
#  "-h": 20,
#  "-l": 30
# }
#}
