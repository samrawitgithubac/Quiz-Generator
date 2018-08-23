# Quiz-Generator
This is a practice exam generator for the Technician Class License Exam

The question pool was found here:
[+] http://ncvec.org/page.php?id=362

The concept here is that the actual exam taken is just a subgroup of the total question pool. The rules for how many questions, and from where they come from, are contained in the actual question pool found here:
[+] http://ncvec.org/downloads/2014-2018%20Tech%20Pool.txt

High-Level Overview:
Creates a database for storage
Parses through the question pool and stores the results in the database for future access
Processes the current user
Generates a valid, random, weighted test
Presents each question to the users
Evaluates the users response
Stores the users results in the database
