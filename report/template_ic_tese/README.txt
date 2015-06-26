Institute of Computing - University of Campinas
Instructions of usage and information of LaTeX IC model.
See the contributors for this class in the file CONTRIBUTORS.txt
Doubts and problems mail info-cpg at ic dot unicamp dot br
--------------------------------------------------------------------------------
You should follow this instructions to keep your thesis in accordance with
PRPG.

	The file ic-tese-v2.cls is a class file, you should inexorable use it. You
can modify the file, but it is on your own risk. Any problem you find you
should mail the CPG.

	The file tese-example-v2.tex is a tex file which contains the right usage
of the latex class file. You should use it replacing the content of the
commands with yours. Note that the commands order should be kept.

	We like to use tabulation, because it is easier to modify the number of
spaces shown. Thus, all the documents here are using tabs instead of spaces. In
spite of this, you can change tab for spaces in your beloved tex editor.

We reproduce here the instructions of the file tese-exemple-v2.tex for class
usage. If you have to use the CoTutela option, comment the line ]%.
\documentclass[%
	% Use this line to thesis with more than 100 pages in ARABIC NUMERATION.
	% Or remove it to thesis with up to 100 pages in ARABIC NUMBERATION.
	TwoSidePages,%
	% Select one of the following idioms to be the main language of your
	% thesis.  If you remove this line the main language will be English.
	English,% Spanish % Portuguese
	% This line set your thesis up as the reviewed version after the defense.
	% Remove this line if you have not defended yet. 
	FinalVersion,%
	% If you intend to use a copyright page, check with CPG or your advisor
	% before. There is complex legal questions with strong consequences.
	Copyright,%
	% Let this command to show the list of your tables. Or removed it.
	TablesPage,%
	% Let this command to show the list of your figures. Or removed it.
	FiguresPage,%
	% You have to use coadvisor's command to set the second supervisor's name.
	% Use this command only if you have done a work with co-supervision
	% (co-tutela) at foreign universities.
	%CoTutela]%
	]%
{ic-tese-v2}

Note the meaning of each option. They have to be used in the right way.
Now, let us observe the commands provide by the class.

\thetitle{TITLE1}{TITLE2}
TITLE1 is the foreign title. English or Spanish. We advise you to write it even
if you are writing in Portuguese.
TITLE2 is the Portuguese title. Note that if you choose to write in Portuguese
the TITLE1 may be cleared, but keep the braces (curly brackets). 
	
\thisyear{YEAR}
YEAR will appear in the title page, and does not have relation with the defense
date.
	
\author{AUTHOR}
AUTHOR is your full name!

\degreesought{DEGREE} 
DEGREE is one of the following options: PhD; MSc; Doctorado; Mag\'ister. Of
course, it depends of your option to main language.

\degreesoughtpt{DEGREEPT}
DEGREEPT have to be inexorable used, despite the main language. You can set it
as: Doutorado; Mestrado.

\titlesought{TITLE}
TITLE is one of the following options: Doutor; Doutora; Mestre; Maestro;
Maestra; PhD; Doctor(if you are using Spanish); Doctora.

\titlesoughtpt{TITLEPT}
TITLEPT have to be inexorable used, despite the main language. You can set it
as: Doutor; Doutora; Mestre; Mestra.

\dept{DEPARTMENT}
DEPARTMENT may be your lab or your department in IC. The command is disused.

\principaladvisor{ADVISOR}
ADVISOR is your advisor's name.

\advisortitle{TITLE/TITLEPT}
This command sets the title that will appear in the examiner board page. Here
is the tricky part. If the main language is Portuguese, just write the TITLEPT.
If the main language is a foreign idiom, write TITLE/\texit{TITLEPT}. TITLE may
be: Supervisor; Director; Directora. TITLEPT: Orientador; Orientadora.

\coadvisor{NAME}
NAME is your coadvisor's name. This command can be omitted, if it is removed.

\coadvisortitle{(TITLE/TITLEPT)\\SCHOOL}
This command sets the title that will appear in the examiner board page. The
usage is the same of the \advisortitle, except for the school's name of the
co-supervisor. This command has no effect is the class option CoTutela is not
active. Here is an example of usage
\coadvisortitle{(Supervisor/\textit{Orientador})\\Massachusetts Institute of
Technology - MIT}

\firstreader{READER\\SCHOOL} 
\secondreader{READER\\SCHOOL}  
\thirdreader{READER\\SCHOOL}  
\fourthreader{READER\\SCHOOL}
\fifthreader{READER\\SCHOOL}
\sixthreader{READER\\SCHOOL}
\seventhreader{READER\\SCHOOL}
All above commands set the name of the READER and the SCHOOL that he/she is
from. You should take attention that substitute readers are defined by
(substitute word in the main language/\textit{Suplente}). For example:
\seventhreader{Prof. Dr. Member 7\\Institute of Computing - UNICAMP
(Substitute/\textit{Suplente})}

\grants{TEXT}
TEXT is the text that you have to use to specify who funds you. Every
foundation discloses rules to do it, you should take a look in the foundation's
website. If you do not have any financial support, you can omit this command,
removing it.

\defencedate{DAY}{MONTH}{YEAR}.
As easy as it seems to be.

\copyrightyear{YEAR}
If you set the option Copyright in the documentclass declaration, you should
specify the year. Note that this command has no effect when the Copyright
option is not used. Besides, you should consult the CPG for legal issues about
using the copyright page in your thesis.

\fichacatalografia{FILE}
\assinaturabanca{FILE}
\folhaderosto{FILE}
Use these commands to replace the original pages in the thesis by the modified
pages provide by CPG or IMEEC library. All these commands work in the same way.
FILE is the location of a PDF file. You can omit the PDF extension.
\fichacatalografica{} is the library register page. \assinaturabanca{} is the
examiner board signatures page. \folhaderosto{} is the advisor's signature
page.

################################################################################
Now, we will describe some complex commands.

\beforepreface command creates the title pages, a copyright page (optionally),
etc. After this command, you should use the commands explained below.

\prefacesection{SECTION} command creates title for sections like abstract and
acknowledgements. You should take a look into the tese-exemple-v2.tex to see
more details.

\theabstract uses the command \prefacesection{Abstract} to create a section
to insert the abstract in English with correct hyphenation.
\elresumen uses the command \prefacesection{Resumen} to create a section
to insert the abstract in Spanish with correct hyphenation.
\oresumo uses the command \prefacesection{Resumo} to create a section
to insert the abstract in Portuguese with correct hyphenation.

\begin{dedico}{ENVIRONMENT}
\end{dedico}
The dedico environment allows create pages for dedication, epigraph, and others
of the kind.

\mylist{COMMANDS}
COMMANDS are the commands that the user need to set your additional lists up.
Lists as abbreviation and others should be instantiated into the mylist
command.

\afterpreface command generates the standard lists, like summary, list of
tables, etc, and the user lists set into the mylist command as well.

Between the \beforepreface and \afterpreface commands everything is printed
in odd pages, numbered by ROMAN numbers. Thus, even pages are left in blank.
After the \afterpreface the thesis text actually starts and the text is
printed in both even and odd pages, numbered by ARABIC numbers.
