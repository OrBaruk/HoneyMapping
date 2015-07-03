% Institute of Computing - University of Campinas
% LaTeX document class for thesis
% See the contributors for this class in the file CONTRIBUTORS.txt
% Before you starts using this class read the file README.txt
% Doubts and problems mail info-cpg at ic dot unicamp dot br

\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{ic-tese-v2}[2014/02/11 Institute of Computing Latex class]
\typeout{Style: TESE IC - UNICAMP <11 de Fevereiro de 2014>.}

\DeclareOption{TwoSidePages}{%
        \PassOptionsToClass{twoside}{report}
        \typeout{Information: Two side pages option is active.}
}
\def\thesislanguage#1{\gdef\@thesislanguage{#1}}
\DeclareOption{English}{%
        \thesislanguage{1}
        \PassOptionsToPackage{brazil, english}{babel}
        \typeout{Information: Now english is the main language of this document.}
}
\DeclareOption{Spanish}{%
        \thesislanguage{2}
        \PassOptionsToPackage{brazil, english, spanish}{babel}
        \typeout{Information: Now spanish is the main language of this document.}
}
\DeclareOption{Portuguese}{%
        \thesislanguage{3}
        \PassOptionsToPackage{english, brazil}{babel}
        \typeout{Information: Now portuguese is the main language of this document.}
}
\newif\iffinalversion
\DeclareOption{FinalVersion}{%
        \finalversiontrue
        \typeout{Information: This document was set as the final version reviewed after the defense.}
}
\newif\ifcopyright
\DeclareOption{Copyright}{%
        \copyrighttrue
        \typeout{Information: A copyright page for this document is active.}
}
\newif\iftablespage
\DeclareOption{TablesPage}{%
        \tablespagetrue
        \typeout{Information: The list of tables in this document will be shown.}
}
\newif\iffigurespage
\DeclareOption{FiguresPage}{%
        \figurespagetrue
        \typeout{Information: The list of figures in this document will be shown.}
}
\newif\ifcotutela
\DeclareOption{CoTutela}{%
        \cotutelatrue
        \typeout{Information: Co-Tutela option is now active.}
}

\ExecuteOptions{English}

\ProcessOptions\relax
\LoadClass[a4paper,12pt]{report}

\RequirePackage{multirow}
\RequirePackage{array}
\RequirePackage{graphicx}
\RequirePackage{babel}
\RequirePackage{datetime}
\typeout{The Warning: No month names provided for language 'brazil' on input   %
Should be ignored. There is a backend processing for the brazilian month names.   }
\RequirePackage{epstopdf}
\RequirePackage{slantsc}
\RequirePackage{lmodern}
\RequirePackage{pdfpages}

\RequirePackage{geometry}
\geometry{a4paper,top=30mm,bottom=33mm,left=35mm,right=22mm}

%This style uses interline spacing that is 1.1 times normal, except
%in the figure and table environments where normal spacing is used.
%That can be changed by doing:
%    \renewcommand{\baselinestretch}{1.6}\small\normalsize
%(or whatever you want instead of 1.6).

% First thing we do is make sure that report has been loaded.  A
% common error is to try to use ic-tese as a documentstyle or class.
\@ifundefined{chapter}{\@latexerr{The `ic-tese' option should be
used with the `report' document style}{You should probably read
the ic-tese documentation.}}{}

% Theses with more than 100 pages must be double-sided, so we have
% to set \evensidemargin, too.
%\oddsidemargin 1cm
%\evensidemargin -0.4cm
%\marginparwidth 40pt \marginparsep 10pt
%\topmargin -1.25cm \headsep .5in
%\textheight 21.5cm \textwidth 16cm

% Use 1.1 times the normal baseline-to-baseline skip
\renewcommand{\baselinestretch}{1.1}

% Redefine the macro used for floats (including figures and tables)
% so that single spacing is used.
% (Note \def\figure{\@float{figure}set single spacing} doesn't work
% because figure has an optional argument)
\let\@xflo@t=\@xfloat
\def\@xfloat{%
\def\baselinestretch{1}\@normalsize
\@xflo@t}


% Redefine the macro used for footnotes to use single spacing
\long\def\@footnotetext#1{\insert\footins{\def\baselinestretch{1}\footnotesize
    \interlinepenalty\interfootnotelinepenalty
    \splittopskip\footnotesep
    \splitmaxdepth \dp\strutbox \floatingpenalty \@MM
    \hsize\columnwidth \@parboxrestore
   \edef\@currentlabel{\csname p@footnote\endcsname\@thefnmark}\@makefntext
    {\rule{\z@}{\footnotesep}\ignorespaces
      #1\strut}}}

% Define current year
\def\thisyear#1{\gdef\@thisyear{#1}}

% Define title in Portuguese
\def\titlept#1{\gdef\@titlept{#1}}

% Define the command that informs which language the thesis is being written.
%\ifcase\@thesislanguage\relax%
%       \or     \selectlanguage{english}%
%       \or             \selectlanguage{spanish}%
%       \else   \selectlanguage{brazil}%
%\fi

% Format the titles
\newcommand{\thetitle}[2]{
        \ifcase\@thesislanguage\relax%
                \or             \title{#1}\titlept{\textit{#2}}
                \or             \title{#1}\titlept{\textit{#2}}
                \else   \title{#2}\titlept{#2}
        \fi
}

% Hacking the report class to not uppercase the bibliography name in the header.
%\renewenvironment{thebibliography}[1]
%     {\chapter*{\bibname}%
%      \@mkboth{\bibname}{\bibname}%
%      \list{\@biblabel{\@arabic\c@enumiv}}%
%           {\settowidth\labelwidth{\@biblabel{#1}}%
%            \leftmargin\labelwidth
%            \advance\leftmargin\labelsep
%            \@openbib@code
%            \usecounter{enumiv}%
%            \let\p@enumiv\@empty
%            \renewcommand\theenumiv{\@arabic\c@enumiv}}%
%      \sloppy
%      \clubpenalty4000
%      \@clubpenalty \clubpenalty
%      \widowpenalty4000%
%      \sfcode`\.\@m}
%     {\def\@noitemerr
%       {\@latex@warning{Empty `thebibliography' environment}}%
%      \endlist}

% \author, \title are defined in report; here are the rest of the
% front matter defining macros
\def\grants#1{\gdef\@grants{#1}}
\def\dept#1{\gdef\@dept{#1}}
\def\principaladvisor#1{\gdef\@principaladvisor{#1}}
\def\principaladviser#1{\gdef\@principaladvisor{#1}}
\def\advisortitle#1{\gdef\@advisor{#1}}
\def\advisertitle#1{\gdef\@advisor{#1}}
\def\firstreader#1{\gdef\@firstreader{#1}}
\def\coadvisor#1{\gdef\@coadvisor{#1}}
\def\coadviser#1{\gdef\@coadvisor{#1}}
\def\coadvisortitle#1{\gdef\@coadvisortitle{#1}}
\def\coadvisertitle#1{\gdef\@coadvisortitle{#1}}
\def\secondreader#1{\gdef\@secondreader{#1}}
\def\thirdreader#1{\gdef\@thirdreader{#1}}
\def\fourthreader#1{\gdef\@fourthreader{#1}}
\def\fifthreader#1{\gdef\@fifthreader{#1}}
\def\sixthreader#1{\gdef\@sixthreader{#1}}
\def\seventhreader#1{\gdef\@seventhreader{#1}}


%ficha
\def\fichacatalografica#1{\gdef\@fichacatalografica{#1}}
%assinaturas
\def\assinaturabanca#1{\gdef\@assinaturabanca{#1}}
%folha de rosto
\def\folhaderosto#1{\gdef\@folhaderosto{#1}}

%
% Force the reference to the document to be:
% - ``Tese'' de Doutorado
% - ``Dissertacao'' de Mestrado
\def\degreesought#1{\gdef\@degreesought{#1}}
\newcommand{\tese}{
% Conditionality for Language
\ifcase\@thesislanguage\relax%
        %English
        \or
        {
                \def\@MSc{MSc}
                \ifx\@MSc\@degreesought
                        \gdef\@thesis{Dissertation}%
                \else
                        \gdef\@thesis{Thesis}%
                \fi%
        }
        %Espanol
        \or
        {
                \def\@MSc{Mag\'ister}
                \ifx\@MSc\@degreesought
                        \gdef\@thesis{Dissertac\'ion}%
                \else
                        \gdef\@thesis{Tesis}%
                \fi%
        }
        %Portugues
        \else
        {
                \relax%
        }
\fi
% End Conditionality
}

\def\@Mestrado{Mestrado}
\def\degreesoughtpt#1{\gdef\@degreesoughtpt{#1}\ifx\@Mestrado\@degreesoughtpt
\gdef\@tesept{Disserta\c{c}{\~a}o}\else\gdef\@tesept{Tese}\fi}%
\degreesoughtpt{Mestrado} % Default

% End Conditionality
%
\def\titlesought#1{\gdef\@titlesought{#1}}%
\def\titlesoughtpt#1{\gdef\@titlesoughtpt{#1}}%
% Commented by Caio
%\def\submitdate#1{\gdef\@submitdate{#1}}
%\def\date#1{\gdef\@submitdate{#1}}
\def\defencedate#1#2#3{
% Conditionality for Language
\ifcase\@thesislanguage\relax%
    %English
    \or
    {
        \gdef\@defencedate{
                        \monthname[#2]\ #1, #3
                }
    }
    %Espanol
    \or
    {
                \gdef\@defencedate{
                        #1\ de\ \monthname[#2]\ de\ #3
                }
    }
    %Portugues (gambis)
    \else
    {
                \gdef\@defencedate{
                        #1\ de\ \ifcase#2\relax
                                        \or janeiro
                                        \or fevereiro
                                        \or mar\c{c}o
                                        \or abril
                                        \or maio
                                        \or junho
                                        \or julho
                                        \or agosto
                                        \or setembro
                                        \or outubro
                                        \or novembro
                                        \or dezembro
                                        \fi de\ #3
                }
    }
\fi
% End Conditionality
}

\def\copyrightyear#1{\gdef\@copyrightyear{#1}}
\def\@title{}\def\@author{}\let\@dept\relax\let\@grants\relax

\newcommand{\faculty}{
% Conditionality for Language
        \ifcase\@thesislanguage\relax%
                %English
                \or %
                        Institute of Computing
                %Espanol
                \or %
                        Instituto de la Computac\'ion
                %Portuguese
                \else %
                        \relax%
        \fi
% End Conditionality
}
\newcommand{\university}{
% Conditionality for Language
        \ifcase\@thesislanguage\relax%
                %English
                \or %
                        University of Campinas
                %Espanol
                \or %
                        Universidad de Campinas
                %Portuguese
                \else %
                        \relax%
        \fi
% End Conditionality
}
\def\@facultypt{Instituto de Computa\c{c}{\~a}o}
\def\@universitypt{Universidade Estadual de Campinas}

\def\@principaladvisor{}\def\@advisor{}\def\@firstreader{}\let\@coadvisor\relax\def\@secondreader{}\def\@thirdreader{}\let\@fourthreader\relax\let\@fifthreader\relax\let\@sixthreader\relax\let\@seventhreader\relax
\def\today{\number\the\day{}\space de\space \ifcase\the\month\or
  janeiro\or fevereiro\or mar\c{c}o\or abril\or maio\or junho\or
  julho\or agosto\or setembro\or outubro\or novembro\or dezembro\fi
  \space de \number\the\year}
\let\@fichacatalografica\relax
\let\@assinaturabanca\relax
\let\@folhaderosto\relax
% Old version commented by Caio
%\def\@submitdate{\the\day{}\space de\space\ifcase\the\month\or
%  Janeiro\or Fevereiro\or Mar\c{c}o\or Abril\or Maio\or Junho\or
%  Julho\or Agosto\or Setembro\or Outubro\or Novembro\or Dezembro\fi
%  \space de \number\the\year}
\def\@copyrightyear{\number\the\year}


\def\copyrightpage{%
%        \null\vfill
%        \begin{center}
%                \copyright\ \@author, \@copyrightyear. \\
%                ~~~Todos os direitos reservados.
%        \end{center}
%        \vskip.5in\cleardoublepage
}


%
%\def\notfinalversiontext{This text corresponds to the \tese presented to the Board of Examiners before the defense.\\\textit{Este exemplar corresponde {\`a} reda\c{c}{\~a}o da \@tesept\ apresentada para a Banca Examinadora antes da defesa da \@tesept.}}
%
%\def\finalversiontext{This text corresponds to the final version of the \tese, duly corrected and defended by  \@author\ and approved by the Board of Examiners.\\\textit{Este exemplar corresponde {\`a} reda\c{c}{\~a}o final da \@tesept\ devidamente corrigida e defendida por \@author\ e aprovada pela Banca Examinadora.}}
%

\def\@logounicamp{logo-unicamp-name-line-blk-red-0480.eps}
\def\@logoic{logo-ic-unicamp-slant-line-wht-sky-ora-0480.eps}

\def\finalversionfront{

 \begin{figure}[t]
  \includegraphics[width=2.5cm]{\@logounicamp}
   \hfill
  \includegraphics[width=2.6cm]{\@logoic}
 \end{figure}
        \begin{center}
           \Large\@author \\
           \vskip 2cm
% Conditionality for Language
        \ifcase\@thesislanguage\relax%
                %English
                \or \Large{\bf\@title}\\
                %Espanol
                \or \Large{\bf\@title}\\
                %Portugues
                \else \hfill\\
        \fi
% End Conditionality
           \vskip 2cm
       \Large{\bf\@titlept} \\
      \vfill
      \large
      CAMPINAS \\
       \@thisyear
        \end{center}
}

\def\finalversiontitle{
\vskip -5mm
        \begin{figure}[t]
                \includegraphics[width=2.5cm]{\@logounicamp}
                \hfill
                \includegraphics[width=2.6cm]{\@logoic}
                \vspace{-6pt}
        \end{figure}

        \noindent

% Conditionality for Language
        \ifcase\@thesislanguage\relax%
                %English
                \or {
                                \noindent\begin{minipage}{.4\textwidth}
                                        \centering
                                    \textbf{\university} \\
                                \textbf{\faculty} \\
                                \end{minipage}
                                %
                                \begin{minipage}{.55\textwidth}
                                        \centering
                                        \textbf{\emph{\@universitypt}} \\
                                    \textbf{\emph{\@facultypt}} \\
                                \end{minipage}
                        }
                %Espanol
                \or {
                                \begin{minipage}{.45\textwidth}
                                        \centering
                                     \textbf{\university} \\
                                 \textbf{\faculty} \\
                                \end{minipage}
                                %
                                \begin{minipage}{.52\textwidth}
                                        \centering
                                        \textbf{\emph{\@universitypt}} \\
                                    \textbf{\emph{\@facultypt}} \\
                                \end{minipage}
                        }
                %Portugues
                \else {
                        \centering
                        \textbf{\@universitypt} \\
                    \textbf{\@facultypt} \\
                }
        \fi
% End Conditionality
        \begin{center}
                \vskip .3cm
                \large\bf\@author \\
                \vspace{0.3cm}
% Conditionality for Language
                \ifcase\@thesislanguage\relax%
                        %English
                        \or \Large\@title\vspace{-3pt}
                        %Espanol
                        \or \Large\@title\vspace{-3pt}
                        %Portuguese
                        \else \vspace{0.5in}\Large\@title\vspace{0.4in}
                \fi
% End Conditionality
        \end{center}

        \noindent

% Conditionality for Language
        \ifcase\@thesislanguage\relax%
        %English
        \or
        {
                \ifcotutela{
                        \begin{tabular}{@{}>{\arraybackslash\centering}m{0.9\textwidth}}
                                \small Supervisor(s)/Orientador(es)\tabularnewline
                                \textbf{\@principaladvisor}\tabularnewline
                                \textbf{\@coadvisor}\tabularnewline
                        \end{tabular}
                }\else{
                        \begin{tabular}{@{}>{\arraybackslash\raggedleft}p{0.19\textwidth}>{\arraybackslash\raggedright}p{0.735\textwidth}@{}}
                                \small Supervisor: & \tabularnewline
                                \small \emph{Orientador(a):} & \multirow{-2}{*}{\textbf{\@principaladvisor}} \tabularnewline
                                & \tabularnewline [-12pt]
                                \ifx\@coadvisor\relax\else
                                        \small Co-Supervisor: & \tabularnewline
                                        \small \emph{Co-orientador(a):} & \multirow{-2}{*}{\textbf{\@coadvisor}}
                                \fi
                        \end{tabular}
                }\fi
        }
        %Espanol
        \or
        {
                \ifcotutela{
                        \begin{tabular}{@{}>{\arraybackslash\centering}m{0.9\textwidth}}
                                \small Director(es)/Orientador(es)\tabularnewline
                                \textbf{\@principaladvisor}\tabularnewline
                                \textbf{\@coadvisor}\tabularnewline
                        \end{tabular}
                }\else{
                        \begin{tabular}{@{}>{\arraybackslash\raggedleft}p{0.19\textwidth}>{\arraybackslash\raggedright}p{0.735\textwidth}@{}}
                                \small Director(a): & \tabularnewline
                                \small \emph{Orientador(a):} & \multirow{-2}{*}{\textbf{\@principaladvisor}}\tabularnewline
                                & \tabularnewline [-12pt]
                                \ifx\@coadvisor\relax\else
                                        \small Co-Director(a): & \tabularnewline
                                        \small \emph{Co-orientador(a):} & \multirow{-2}{*}{\textbf{\@coadvisor}}
                                \fi
                        \end{tabular}
                }\fi
        }
        %Portugues
        \else
        {
                \ifcotutela{
                        \vspace*{-24pt}
                        \begin{tabular}{@{}>{\arraybackslash\centering}m{0.9\textwidth}}
                                \small Orientador(es)\tabularnewline
                                \textbf{\@principaladvisor}$^1$\tabularnewline
                                \textbf{\@coadvisor}$^2$\tabularnewline
                        \end{tabular}
                        \vspace*{6pt}
                }\else{
                        \vspace*{-24pt}
                        \begin{tabular}{@{}>{\arraybackslash\raggedleft}p{0.19\textwidth}>{\arraybackslash\raggedright}p{0.735\textwidth}@{}}
                                \small Orientador(a): & \textbf{\@principaladvisor}\tabularnewline
                                & \tabularnewline [-12pt]
                                \ifx\@coadvisor\relax\else
                                        \small Co-Orientador(a): & \textbf{\@coadvisor}\
                                \fi
                        \end{tabular}
                        \vspace*{6pt}
                }\fi
        }
        \fi
% End Conditionality

% Conditionality for Language
        \ifcase\@thesislanguage\relax%
                %English
                \or
                 {
                        \begin{center}
                                \vspace{-3pt}
                                \Large\bf\textit{\@titlept}
                        \end{center}
                }
                %Espanol
                \or
                 {
                        \begin{center}
                                \vspace{-6pt}
                                \Large\bf\textit{\@titlept}
                        \end{center}
                }
                %Portugues
                \else
                {
                        \relax
                }
        \fi
% End Conditionality

        \noindent

% Conditionality for Language
        \tese
        \ifcase\@thesislanguage\relax%
        %English
        \or
        {
                \iffinalversion
                        \def\textaboutversion{
                                {\small \textsc{This volume corresponds to the final version of the \@thesis\ defended by \@author, under the supervision of ~\@principaladvisor.}} &
                                {\foreignlanguage{brazil}{\small \slshape \scshape Este exemplar corresponde \`{a} vers{\~a}o final da \@tesept\ defendida por \@author, sob orienta\c{c}{\~a}o de ~\@principaladvisor.}}
                        }
                \else
                        \def\textaboutversion{
                                {\small \textsc{This volume corresponds to the version of the \@thesis\ submitted to examining board by \@author, under the supervision of ~\@principaladvisor.}} &
                                {\foreignlanguage{brazil}{\small \slshape \scshape Este exemplar corresponde \`{a} vers{\~a}o da \@tesept\ apresentada \`{a} banca examinadora por \@author, sob orienta\c{c}{\~a}o de ~\@principaladvisor.}}
                        }
                \fi

                \hspace*{-24pt}
                \noindent\begin{minipage}[!h]{\textwidth}
                        \center
                        \begin{tabular}{@{}p{.50\textwidth}p{.50\textwidth}@{}}
                                {\small\@degreesought\ \@thesis\ presented to the Graduate Program of the \faculty of the \university to obtain a \@titlesought\ degree in Computer Science.} &
                                {\foreignlanguage{brazil}{\small \emph{\@tesept\ de \@degreesoughtpt\ apresentada ao Programa de P\'os-Gradua\c{c}{\~a}o em Ci\^encia da Computa\c{c}{\~a}o do \@facultypt\ da \@universitypt\ para obten\c{c}{\~a}o do t{\'\i}tulo de \@titlesoughtpt\ em Ci{\^e}ncia da Computa\c{c}{\~a}o.}}} \tabularnewline
                                & \tabularnewline[-6pt]
                                \textaboutversion
                        \end{tabular}
                \end{minipage}
        }
        %Espanol
        \or
        {
                \iffinalversion
                        \def\textaboutversion{
                                {\small \textsc{Este ejemplo corresponde a la versi\'on final de la \@thesis\ defendida por \@author, bajo de la direcci\'on de ~\@principaladvisor.}} &
                                {\foreignlanguage{brazil}{\small \slshape \scshape Este exemplar corresponde \`{a} vers{\~a}o final da \@tesept\ defendida por \@author, sob orienta\c{c}{\~a}o de ~\@principaladvisor.}}
                        }
                \else
                        \def\textaboutversion{
                                {\small \textsc{Este ejemplo corresponde a la versi\'on de la \@thesis\ presentada al jurado examinador por \@author, bajo de la direcci\'on de ~\@principaladvisor.}} &
                                {\foreignlanguage{brazil}{\small \slshape \scshape Este exemplar corresponde \`{a} vers{\~a}o da \@tesept\ apresentada \`{a} banca examinadora por \@author, sob orienta\c{c}{\~a}o de ~\@principaladvisor.}}
                        }
                \fi

                \hspace*{-24pt}
                \noindent\begin{minipage}[!h]{\textwidth}
                        \center
                        \begin{tabular}{@{}p{.50\textwidth}p{.50\textwidth}@{}}
                                {\small\@thesis\ de \@degreesought\ presentada al Programa de Postgrado del \faculty de la \university para obtener el t\'itulo de \@titlesought\ en Ciencias de la Computaci\'on.} &
                                {\foreignlanguage{brazil}{\small\emph{\@tesept\ de \@degreesoughtpt\ apresentada ao Programa de P\'os-Gradua\c{c}{\~a}o em Ci\^encia da Computa\c{c}{\~a}o do \@facultypt\ da \@universitypt\ para obten\c{c}{\~a}o do t{\'\i}tulo de \@titlesoughtpt\ em Ci{\^e}ncia da Computa\c{c}{\~a}o.}}}\tabularnewline
                                & \tabularnewline[-6pt]
                                \textaboutversion
                        \end{tabular}
                \end{minipage}
        }
        %Portugues
        \else
        {
                \iffinalversion
                        \def\textaboutversion{
                                {\small\textsc{Este exemplar corresponde \`{a} vers{\~a}o final da \@tesept\ defendida por \@author, sob orienta\c{c}{\~a}o de ~\@principaladvisor.}}
                        }
                \else
                        \def\textaboutversion{
                                {\small \textsc{HUEHUEHUEHUEste exemplar corresponde \`{a} vers{\~a}o da \@tesept\ apresentada \`{a} banca examinadora por \@author, sob orienta\c{c}{\~a}o de ~\@principaladvisor.}}
                        }
                \fi
                        \begin{tabular}{@{}p{.9\textwidth}}
                                \begin{flushleft}
                                \hspace*{0.3\textwidth}\@tesept\ de \@degreesoughtpt\ apresentada ao Programa de P\'os-Gradua\c{c}{\~a}o em Ci\^encia da Computa\c{c}{\~a}o do \@facultypt\ da \@universitypt\ para obten\c{c}{\~a}o do t{\'\i}tulo de \@titlesoughtpt\ em Ci{\^e}ncia da Computa\c{c}{\~a}o.
                                \end{flushleft}
                        \end{tabular}

                \vspace{12pt}

                \begin{minipage}[!h]{0.45\textwidth}
                        \textaboutversion
                \end{minipage}
        }
        \fi
% End Conditionality
        \vskip 1cm

% Co-supervision test
        \ifcotutela{
                \hspace*{-22pt}
                \begin{minipage}[!h]{\textwidth}
                    \begin{center}
                        \rule{.43\textwidth}{1pt} \qquad \rule{.43\textwidth}{1pt} \\
% Conditionality for Language
                        \ifcase\@thesislanguage\relax%
                        %English
                        \or {\small \qquad Supervisor's signature \hspace*{1.3in} \emph{Assinatura do Orientador(a)}}
                        %Espanol
                        \or {\small \qquad Firma de Director(a) \hspace*{1.3in} \emph{Assinatura do Orientador(a)}}
                        %Portugues
                        \else {\small $^1$Assinatura do Orientador(a) \hspace*{1.1in} $^2$Assinatura do Orientador(a)}
                    \fi\\
% End Conditionality
                \vspace{.25cm}
                        CAMPINAS \\
                        \@thisyear
                        \end{center}
                \end{minipage}
        }\else{
                \hspace*{-22pt}
                \begin{minipage}[!h]{\textwidth}
                        \vspace*{-0.3cm}
                    \begin{center}
                    \rule{.56\textwidth}{1pt} \\
% Conditionality for Language
                        \ifcase\@thesislanguage\relax%
                        %English
                        \or {\small Supervisor's signature / \emph{Assinatura do Orientador(a)}}
                        %Espanol
                        \or {\small Firma de Director(a)/ \emph{Assinatura do Orientador(a)}}
                        %Portugues
                        \else {\small Assinatura do Orientador(a)}
                        \fi\\
% End Conditionality
                        \vspace{.25cm}
                        CAMPINAS \\
                        \@thisyear
                        \end{center}
                \end{minipage}
        }\fi
}

\newenvironment{theabstract}{\prefacesection{Abstract}\foreignlanguage{english}}{\cleardoublepage}
\newenvironment{elresumen}{\prefacesection{Resumen}\foreignlanguage{spanish}}{\cleardoublepage}
\newenvironment{oresumo}{\prefacesection{Resumo}\foreignlanguage{brazil}}{\cleardoublepage}

\def\fichacatalograficapage%
{
        \ifx\@fichacatalografica\relax%
                \begin{center}
                        %\thispagestyle{empty}
                        \vspace{10cm}
                        {\Large\bf\expandafter{Substitua pela ficha catalogr{\'a}fica}\\
                        {\rm (Esta p{\'a}gina deve ser o verso da p{\'a}gina anterior mesmo no\\
                        caso em que n{\~a}o se imprime frente e verso, i.e. at{\'e} 100 p{\'a}ginas.)}}
                        %\addtocounter{page}{-1}
                \end{center}
        \else%
                \includepdf[pagecommand={}]{\@fichacatalografica}
        \fi
}

%\def\fichacatalografica{
%  \begin{center}
%%    \thispagestyle{empty}
%    \vspace{10cm}
%    {\Large\bf\expandafter{Substitua pela ficha catalogr{\'a}fica}\\
%    {\rm (Esta p{\'a}gina deve ser o verso da p{\'a}gina anterior mesmo no\\
%    caso em que n{\~a}o se imprime frente e verso, i.e. at{\'e} 100 p{\'a}ginas.)}}
%%    \addtocounter{page}{-1}
%  \end{center}
%}

\def\assinaturabancapage
{
        \ifx\@assinaturabanca\relax%
                \begin{center}
                        \vspace{10cm}
                        \Large\bf\expandafter{Substitua pela folha com as assinaturas da banca}
                \end{center}
        \else%
                \includepdf[pagecommand={}]{\@assinaturabanca}
        \fi
}
%\def\assinaturabanca{
%  \begin{center}
%    \vspace{10cm}
%    \Large\bf\expandafter{Substitua pela folha com as assinaturas da banca}
%  \end{center}
%}

\def\windowtitle{\bgroup\newpage\c@page\z@
%  \thispagestyle{empty}
  \parindent 0pt
  \small\rm             % \xipt
  \null\vskip 12.9cm
\begin{center}
\hskip-1.75cm
\framebox[10.5cm]{
  \vbox to 5.75cm{\vfill
\hsize=3.5575in\textwidth=\hsize\linewidth=\hsize
\begin{center}
\vbox{
   \begin{center}
    \def\thanks##1{}
    \def\@footnotemark{\relax}
    {\bf \@title \par}
    \vskip 1.5ex
    {\it
       \begin{tabular}[t]{c}
       \def\and{
       %%\begin{tabular}
       \end{tabular}\hskip 1em plus .17fil\begin{tabular}[t]{c}
       %% \end{tabular}
       }
       \@author
       end{tabular}\par
    }
    \vskip 1.5ex
    {\bf \@tesept\ de \@degreesoughtpt}
   \end{center}
}\end{center}
  \vfill}
}\end{center}
\egroup}

% PATCH: Here, I fix \cleardoublepage so that the skipped pages are really blank! PJR
%    \let\origdoublepage\cleardoublepage
    \newcommand{\clearemptydoublepage}{%
%      \clearpage
%      {\pagestyle{empty}\origdoublepage}%
    }
%    \let\cleardoublepage\clearemptydoublepage
% MORE AGGRESSIVE PATCH: Do not let a text starts in an even numbered page. CH
%    \let\origdoublepage\cleardoublepage
%    \newcommand{\clearemptydoublepage}{%
%      \clearpage
%      {\pagestyle{empty}\origdoublepage
%               \ifodd\c@page\thispagestyle{empty}\clearpage\fi
%       }
%    }
%    \let\cleardoublepage\clearemptydoublepage

%%%%%%%%%%%% Set on/off even pages as blank pages %%%%%%%%%%%%
\def\documentsetup#1{
%        \ifcase#1
%        %\if@twoside
%                \let\@outputpage\ol@outputpage
%        %\fi
%        \else%
%                \let\ol@outputpage\@outputpage
%                \def\@outputpage{%
%                \ifodd\c@page\else\shipout\vbox{}\advance\c@page\@ne\fi
%                \ol@outputpage}
%        \fi
}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\def\beforepreface{
        \pagenumbering{roman}
        \pagestyle{plain}
  %        \windowtitle
        \finalversionfront
  \if@twoside
  \cleardoublepage
  \else
  \clearpage\
  \fi
%\rule{0pt}{4ex}
% A primeira folha interna e a página de rosto devem ser ambas de ``frente''.
%        \newpage
%        \mbox{}
%        \newpage

  \ifx\@folhaderosto\relax%
  \finalversiontitle
  \else
  \includepdf[pagecommand={}]{\@folhaderosto}
  \fi


% Insert a \clearemptydoublepage in case this is not a final version
% to separate \finalversiontitle from \titlep when \finalversionfalse is set.
% Collapsed both \fichacatalografica and \assinaturabanca in a single if.
  \iffinalversion%

  \clearpage
  \fichacatalograficapage\clearemptydoublepage%
  \if@twoside
  \cleardoublepage
  \else
  \clearpage
  \fi

  \assinaturabancapage\clearemptydoublepage%
  \if@twoside
  \cleardoublepage
  \else
  \clearpage
  \fi

  \else
  \if@twoside
  \cleardoublepage
  \else
  \clearpage
  \fi
  \fi

%%%%%%%%%% Make the text just be written in odd pages  %%%%%%%%%%
        \if@twoside\relax\else
                \documentsetup{1} % enable
        \fi
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    \titlep
    \ifcopyright\clearemptydoublepage\copyrightpage\fi\clearemptydoublepage
}

\def\prefacesection#1{%
    \clearemptydoublepage
    \chapter*{#1}
    \addcontentsline{toc}{chapter}{#1}
    }

\newenvironment{dedico}[1]{
  \vspace*{0.7\textheight}
  \phantomsection
  %\addcontentsline{toc}{chapter}{#1}
  \chaptermark{#1}
  \begin{flushright}
    \begin{minipage}[l]{0.45\textwidth}
}
{
  \end{minipage}
  \end{flushright}
  \vfill
%  \pagebreak
  \if@twoside
  \cleardoublepage
  \else
  \clearpage
  \fi
}

\def\mylists#1{
        \typeout{#1}
        \gdef\@mylists{#1}
}
\mylists{\relax}

\def\afterpreface{
%%%%%%%%%% Make the text just be written in odd pages  %%%%%%%%%%
        \if@twoside
                \documentsetup{1} % enable
        \fi
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        \if@twoside
          \tableofcontents
          \cleardoublepage
          \iftablespage
            \listoftables
            \cleardoublepage
          \fi
          \iffigurespage
            \listoffigures
            \cleardoublepage
          \fi
          \@mylists
          \cleardoublepage
        \else
          \tableofcontents
          \clearpage
          \iftablespage
            \listoftables
            \clearpage
          \fi
          \iffigurespage
            \listoffigures
            \clearpage
          \fi
          \@mylists
          \clearpage
        \fi
%    \listoftables
%    \clearpage
%    \listoffigures
%    \clearpage

%%%%%%%%%% Make the page sequence become normal %%%%%%%%%%%
        \if@twoside
                \documentsetup{0} % disable
        \fi
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%    \if@twoside\ifodd\c@page\else\null\thispagestyle{empty}\clearpage\fi\fi

%%%%%%%%%% Make the page sequence become normal %%%%%%%%%%%
%        \if@twoside\relax\else
%                \documentsetup{0} % disable
%                \ifodd\c@page\else % <--- OMG! I have to do it, I'm so sorry. :-(
%                        \vbox{}\thispagestyle{empty}
%                        \clearpage
%                \fi
%        \fi
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

    \@openrighttrue
    \pagenumbering{arabic}
    \pagestyle{headings}

}


%%%%%% Change requested by CCPG %%%%%%%
%\def\afterpreface{
%       \clearemptydoublepage
%    \tableofcontents
%    \clearemptydoublepage
%    \iftablespage
%        \listoftables
%        \clearemptydoublepage
%    \fi
%    \iffigurespage
%        \listoffigures
%        \clearemptydoublepage
%    \fi
%    \if@twoside\ifodd\c@page\else\null\thispagestyle{empty}\clearpage\fi\fi
%    \@openrighttrue
%    \pagenumbering{arabic}
%    \pagestyle{headings}
%    }

\def\ps@headings{\let\@mkboth\markboth
\def\@oddfoot{}\def\@evenfoot{}%
\def\@evenhead{\rm \thepage\hfil \sl \leftmark}%
\def\@oddhead{\hbox{}\sl \rightmark \hfil \rm\thepage}%
\def\chaptermark##1{\markboth {{\ifnum \c@secnumdepth >\m@ne
\@chapapp\ \thechapter. \ \fi ##1}}{}}%
\def\sectionmark##1{\markright {{\ifnum \c@secnumdepth >\z@
\thesection. \ \fi ##1}}}}

% Redefine \thebibliography to go to a new page and put an entry in the
% table of contents
\let\@ldthebibliography\thebibliography
\renewcommand{\thebibliography}[1]{\newpage\cleardoublepage\phantomsection
        \addcontentsline{toc}{chapter}{\bibname}
        \@ldthebibliography{#1}}

% Start out normal
\pagestyle{headings}
