LOAD DATA
INFILE './data/PHYSICALPARTSTREE.dat' 
BADFILE './data/PHYSICALPARTSTREE.bad'
DISCARDFILE './data/PHYSICALPARTSTREE.dsc'
INSERT INTO TABLE CMSINTEGRATION.PHYSICALPARTSTREE
FIELDS TERMINATED by ","
(
 PHYSICALPART_ID CHAR,
 CONTAINERPART_ID CHAR NULLIF CONTAINERPART_ID='',
 LPNAME CHAR
)
