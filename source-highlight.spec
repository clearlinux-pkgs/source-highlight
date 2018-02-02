#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : source-highlight
Version  : 3.1.8
Release  : 27
URL      : ftp://ftp.gnu.org/gnu/src-highlite/source-highlight-3.1.8.tar.gz
Source0  : ftp://ftp.gnu.org/gnu/src-highlite/source-highlight-3.1.8.tar.gz
Summary  : syntax highlighting for source documents
Group    : Development/Tools
License  : GFDL-1.1 GPL-3.0 GPL-3.0+
Requires: source-highlight-bin
Requires: source-highlight-lib
Requires: source-highlight-data
Requires: source-highlight-doc
BuildRequires : bison
BuildRequires : boost
BuildRequires : boost-dev
BuildRequires : flex
BuildRequires : valgrind

%description


%package bin
Summary: bin components for the source-highlight package.
Group: Binaries
Requires: source-highlight-data

%description bin
bin components for the source-highlight package.


%package data
Summary: data components for the source-highlight package.
Group: Data

%description data
data components for the source-highlight package.


%package dev
Summary: dev components for the source-highlight package.
Group: Development
Requires: source-highlight-lib
Requires: source-highlight-bin
Requires: source-highlight-data
Provides: source-highlight-devel

%description dev
dev components for the source-highlight package.


%package doc
Summary: doc components for the source-highlight package.
Group: Documentation

%description doc
doc components for the source-highlight package.


%package lib
Summary: lib components for the source-highlight package.
Group: Libraries
Requires: source-highlight-data

%description lib
lib components for the source-highlight package.


%prep
%setup -q -n source-highlight-3.1.8

%build
%configure --disable-static --with-boost-regex=boost_regex \
--with-bash-completion=/usr/share/bash-completion/completions
make V=1  %{?_smp_mflags}

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check || :

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/check-regexp
/usr/bin/cpp2html
/usr/bin/java2html
/usr/bin/source-highlight
/usr/bin/source-highlight-esc.sh
/usr/bin/source-highlight-settings
/usr/bin/src-hilite-lesspipe.sh

%files data
%defattr(-,root,root,-)
/usr/share/bash-completion/completions/source-highlight
/usr/share/source-highlight/Hello.css
/usr/share/source-highlight/Hello2.css
/usr/share/source-highlight/ada.lang
/usr/share/source-highlight/applescript.lang
/usr/share/source-highlight/asm.lang
/usr/share/source-highlight/awk.lang
/usr/share/source-highlight/bat.lang
/usr/share/source-highlight/bib.lang
/usr/share/source-highlight/bison.lang
/usr/share/source-highlight/c.lang
/usr/share/source-highlight/c_comment.lang
/usr/share/source-highlight/c_string.lang
/usr/share/source-highlight/caml.lang
/usr/share/source-highlight/changelog.lang
/usr/share/source-highlight/clike_vardeclaration.lang
/usr/share/source-highlight/clipper.lang
/usr/share/source-highlight/cobol.lang
/usr/share/source-highlight/coffeescript.lang
/usr/share/source-highlight/conf.lang
/usr/share/source-highlight/cpp.lang
/usr/share/source-highlight/cpp2html.css
/usr/share/source-highlight/csharp.lang
/usr/share/source-highlight/css.lang
/usr/share/source-highlight/css_common.outlang
/usr/share/source-highlight/d.lang
/usr/share/source-highlight/default.css
/usr/share/source-highlight/default.lang
/usr/share/source-highlight/default.style
/usr/share/source-highlight/desktop.lang
/usr/share/source-highlight/diff.lang
/usr/share/source-highlight/docbook.outlang
/usr/share/source-highlight/erlang.lang
/usr/share/source-highlight/errors.lang
/usr/share/source-highlight/esc.outlang
/usr/share/source-highlight/esc.style
/usr/share/source-highlight/esc256.outlang
/usr/share/source-highlight/esc256.style
/usr/share/source-highlight/extreme_comment.lang
/usr/share/source-highlight/extreme_comment2.lang
/usr/share/source-highlight/extreme_comment3.lang
/usr/share/source-highlight/feature.lang
/usr/share/source-highlight/fixed-fortran.lang
/usr/share/source-highlight/flex.lang
/usr/share/source-highlight/fortran.lang
/usr/share/source-highlight/function.lang
/usr/share/source-highlight/glsl.lang
/usr/share/source-highlight/go.lang
/usr/share/source-highlight/groff_man.outlang
/usr/share/source-highlight/groff_mm.outlang
/usr/share/source-highlight/groff_mm_color.outlang
/usr/share/source-highlight/groovy.lang
/usr/share/source-highlight/haskell.lang
/usr/share/source-highlight/haskell_literate.lang
/usr/share/source-highlight/haxe.lang
/usr/share/source-highlight/html.lang
/usr/share/source-highlight/html.outlang
/usr/share/source-highlight/html5.outlang
/usr/share/source-highlight/html5_common.outlang
/usr/share/source-highlight/html_common.outlang
/usr/share/source-highlight/html_notfixed.outlang
/usr/share/source-highlight/html_ref.outlang
/usr/share/source-highlight/html_simple.lang
/usr/share/source-highlight/htmlcss.outlang
/usr/share/source-highlight/htmltable.outlang
/usr/share/source-highlight/htmltablelinenum.outlang
/usr/share/source-highlight/islisp.lang
/usr/share/source-highlight/java.lang
/usr/share/source-highlight/javadoc.outlang
/usr/share/source-highlight/javalog.lang
/usr/share/source-highlight/javalog.style
/usr/share/source-highlight/javascript.lang
/usr/share/source-highlight/json.lang
/usr/share/source-highlight/json.style
/usr/share/source-highlight/key_string.lang
/usr/share/source-highlight/lang.map
/usr/share/source-highlight/langdef.lang
/usr/share/source-highlight/latex.lang
/usr/share/source-highlight/latex.outlang
/usr/share/source-highlight/latexcolor.outlang
/usr/share/source-highlight/ldap.lang
/usr/share/source-highlight/lilypond.lang
/usr/share/source-highlight/lilypond.style
/usr/share/source-highlight/lisp.lang
/usr/share/source-highlight/log.lang
/usr/share/source-highlight/logtalk.lang
/usr/share/source-highlight/lsm.lang
/usr/share/source-highlight/lua.lang
/usr/share/source-highlight/m4.lang
/usr/share/source-highlight/makefile.lang
/usr/share/source-highlight/manifest.lang
/usr/share/source-highlight/mediawiki.outlang
/usr/share/source-highlight/mono-alt.css
/usr/share/source-highlight/mono.css
/usr/share/source-highlight/nohilite.lang
/usr/share/source-highlight/number.lang
/usr/share/source-highlight/odf.outlang
/usr/share/source-highlight/opa.lang
/usr/share/source-highlight/outlang.lang
/usr/share/source-highlight/outlang.map
/usr/share/source-highlight/oz.lang
/usr/share/source-highlight/pascal.lang
/usr/share/source-highlight/pc.lang
/usr/share/source-highlight/perl.lang
/usr/share/source-highlight/php.lang
/usr/share/source-highlight/po.lang
/usr/share/source-highlight/postscript.lang
/usr/share/source-highlight/prolog.lang
/usr/share/source-highlight/properties.lang
/usr/share/source-highlight/proto.lang
/usr/share/source-highlight/python.lang
/usr/share/source-highlight/r.lang
/usr/share/source-highlight/r.style
/usr/share/source-highlight/ruby.lang
/usr/share/source-highlight/s.lang
/usr/share/source-highlight/scala.lang
/usr/share/source-highlight/scheme.lang
/usr/share/source-highlight/script_comment.lang
/usr/share/source-highlight/sexp.outlang
/usr/share/source-highlight/sh.lang
/usr/share/source-highlight/sh_acid.css
/usr/share/source-highlight/sh_berries-dark.css
/usr/share/source-highlight/sh_berries-light.css
/usr/share/source-highlight/sh_bipolar.css
/usr/share/source-highlight/sh_blacknblue.css
/usr/share/source-highlight/sh_bright.css
/usr/share/source-highlight/sh_contrast.css
/usr/share/source-highlight/sh_darkblue.css
/usr/share/source-highlight/sh_darkness.css
/usr/share/source-highlight/sh_desert.css
/usr/share/source-highlight/sh_dull.css
/usr/share/source-highlight/sh_easter.css
/usr/share/source-highlight/sh_emacs.css
/usr/share/source-highlight/sh_golden.css
/usr/share/source-highlight/sh_greenlcd.css
/usr/share/source-highlight/sh_ide-anjuta.css
/usr/share/source-highlight/sh_ide-codewarrior.css
/usr/share/source-highlight/sh_ide-devcpp.css
/usr/share/source-highlight/sh_ide-eclipse.css
/usr/share/source-highlight/sh_ide-kdev.css
/usr/share/source-highlight/sh_ide-msvcpp.css
/usr/share/source-highlight/sh_kwrite.css
/usr/share/source-highlight/sh_matlab.css
/usr/share/source-highlight/sh_navy.css
/usr/share/source-highlight/sh_nedit.css
/usr/share/source-highlight/sh_neon.css
/usr/share/source-highlight/sh_night.css
/usr/share/source-highlight/sh_pablo.css
/usr/share/source-highlight/sh_peachpuff.css
/usr/share/source-highlight/sh_print.css
/usr/share/source-highlight/sh_rand01.css
/usr/share/source-highlight/sh_the.css
/usr/share/source-highlight/sh_typical.css
/usr/share/source-highlight/sh_vampire.css
/usr/share/source-highlight/sh_vim-dark.css
/usr/share/source-highlight/sh_vim.css
/usr/share/source-highlight/sh_whatis.css
/usr/share/source-highlight/sh_whitengrey.css
/usr/share/source-highlight/sh_zellner.css
/usr/share/source-highlight/slang.lang
/usr/share/source-highlight/sml.lang
/usr/share/source-highlight/spec.lang
/usr/share/source-highlight/sql.lang
/usr/share/source-highlight/style.defaults
/usr/share/source-highlight/style.lang
/usr/share/source-highlight/style2.style
/usr/share/source-highlight/style3.style
/usr/share/source-highlight/symbols.lang
/usr/share/source-highlight/tcl.lang
/usr/share/source-highlight/texinfo.lang
/usr/share/source-highlight/texinfo.outlang
/usr/share/source-highlight/texinfo.style
/usr/share/source-highlight/tml.lang
/usr/share/source-highlight/tml_formatting.lang
/usr/share/source-highlight/tml_formatting_all.lang
/usr/share/source-highlight/tml_glue.lang
/usr/share/source-highlight/tml_macrolinks.lang
/usr/share/source-highlight/tml_macros.lang
/usr/share/source-highlight/tml_macros1.lang
/usr/share/source-highlight/tml_macros2.lang
/usr/share/source-highlight/tml_macrosdelayed1.lang
/usr/share/source-highlight/tml_macrosdelayed2.lang
/usr/share/source-highlight/tml_macrosdelayed3.lang
/usr/share/source-highlight/tml_macrotokens.lang
/usr/share/source-highlight/todo.lang
/usr/share/source-highlight/upc.lang
/usr/share/source-highlight/url.lang
/usr/share/source-highlight/vala.lang
/usr/share/source-highlight/vbscript.lang
/usr/share/source-highlight/xhtml.css
/usr/share/source-highlight/xhtml.outlang
/usr/share/source-highlight/xhtml_common.outlang
/usr/share/source-highlight/xhtml_notfixed.outlang
/usr/share/source-highlight/xhtmlcss.outlang
/usr/share/source-highlight/xhtmltable.outlang
/usr/share/source-highlight/xml.lang
/usr/share/source-highlight/xorg.lang
/usr/share/source-highlight/zsh.lang

%files dev
%defattr(-,root,root,-)
/usr/include/srchilite/bufferedoutput.h
/usr/include/srchilite/chartranslator.h
/usr/include/srchilite/colormap.h
/usr/include/srchilite/colors.h
/usr/include/srchilite/ctagscollector.h
/usr/include/srchilite/ctagsformatter.h
/usr/include/srchilite/ctagsmanager.h
/usr/include/srchilite/debuglistener.h
/usr/include/srchilite/delimitedlangelem.h
/usr/include/srchilite/docgenerator.h
/usr/include/srchilite/doctemplate.h
/usr/include/srchilite/eventgenerator.h
/usr/include/srchilite/fileinfo.h
/usr/include/srchilite/fileutil.h
/usr/include/srchilite/formatter.h
/usr/include/srchilite/formatterfactory.h
/usr/include/srchilite/formattermanager.h
/usr/include/srchilite/formatterparams.h
/usr/include/srchilite/highlightbuilderexception.h
/usr/include/srchilite/highlightevent.h
/usr/include/srchilite/highlighteventlistener.h
/usr/include/srchilite/highlightrule.h
/usr/include/srchilite/highlightrulefactory.h
/usr/include/srchilite/highlightstate.h
/usr/include/srchilite/highlightstatebuilder.h
/usr/include/srchilite/highlightstateprinter.h
/usr/include/srchilite/highlighttoken.h
/usr/include/srchilite/instances.h
/usr/include/srchilite/ioexception.h
/usr/include/srchilite/keys.h
/usr/include/srchilite/langdefmanager.h
/usr/include/srchilite/langdefparser.h
/usr/include/srchilite/langdefparserfun.h
/usr/include/srchilite/langdefscanner.h
/usr/include/srchilite/langelem.h
/usr/include/srchilite/langelems.h
/usr/include/srchilite/langelemsprinter.h
/usr/include/srchilite/langmap.h
/usr/include/srchilite/languageinfer.h
/usr/include/srchilite/linebuffer.h
/usr/include/srchilite/linenumgenerator.h
/usr/include/srchilite/lineranges.h
/usr/include/srchilite/matchingparameters.h
/usr/include/srchilite/namedsubexpslangelem.h
/usr/include/srchilite/outlangdefparser.h
/usr/include/srchilite/outlangdefparserfun.h
/usr/include/srchilite/outlangdefscanner.h
/usr/include/srchilite/parserexception.h
/usr/include/srchilite/parserinfo.h
/usr/include/srchilite/parsestruct.h
/usr/include/srchilite/parsestyles.h
/usr/include/srchilite/preformatter.h
/usr/include/srchilite/readtags.h
/usr/include/srchilite/refposition.h
/usr/include/srchilite/regexhighlightrule.h
/usr/include/srchilite/regexpreprocessor.h
/usr/include/srchilite/regexranges.h
/usr/include/srchilite/regexrulefactory.h
/usr/include/srchilite/settings.h
/usr/include/srchilite/sourcefilehighlighter.h
/usr/include/srchilite/sourcehighlight.h
/usr/include/srchilite/sourcehighlighter.h
/usr/include/srchilite/sourcehighlightutils.h
/usr/include/srchilite/srcuntabifier.h
/usr/include/srchilite/statelangelem.h
/usr/include/srchilite/statestartlangelem.h
/usr/include/srchilite/stopwatch.h
/usr/include/srchilite/stringdef.h
/usr/include/srchilite/stringlistlangelem.h
/usr/include/srchilite/stringtable.h
/usr/include/srchilite/stylecssparser.h
/usr/include/srchilite/stylefileparser.h
/usr/include/srchilite/stylekey.h
/usr/include/srchilite/styleparser.h
/usr/include/srchilite/substfun.h
/usr/include/srchilite/textstyle.h
/usr/include/srchilite/textstylebuilder.h
/usr/include/srchilite/textstyleformatter.h
/usr/include/srchilite/textstyleformattercollection.h
/usr/include/srchilite/textstyleformatterfactory.h
/usr/include/srchilite/textstyles.h
/usr/include/srchilite/tostringcollection.h
/usr/include/srchilite/utils.h
/usr/include/srchilite/vardefinitions.h
/usr/include/srchilite/verbosity.h
/usr/include/srchilite/versions.h
/usr/include/srchilite/wordtokenizer.h
/usr/lib64/*.so
/usr/lib64/pkgconfig/*.pc

%files doc
%defattr(-,root,root,-)
%doc /usr/share/doc/source-highlight/*
%doc /usr/share/info/*
%doc /usr/share/man/man1/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/*.so.*
