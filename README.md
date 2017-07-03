# csv2mongo

A tool to import large (max 1-GB) csv files into MongoDB.
Developed for NPSC during MSc Student Placement at the University of Dundee.
Two main lines of development
<ul>
<li>Desktop Based GUI with Python tKinter</li>
<li>Server Based App with Python Flask</li>
</ul>
The data to be stored has a variable structure, therefore a schemaless approach is required.
In MongoDB the schema is defined by the structure of the inserted document.
MongoDB data models express one-to-many relationships with referencing or nesting (more native).
The model uses referencing to describe the relationship between a file and its rows.
Although it should be a hierarchical (nested) relationship, the limit of the documentsize(16MB)
makes it inpossible to insert documents at the file level (up to 1-2GB).
The documents from one experiment are grouped into collections.
Collections of individual users are grouped into databases.

The database will be used as a data source in Spotfire High Content Profiler,
Python scripts and R.
Spotfire requires a tabular based input.
Database connector (ODBC) should be used to provide a tabular interface for MongoDB.
The documents are inserted by Python in hierarchical dict format,
therefore the data will be easilly digested in both Python and R.
