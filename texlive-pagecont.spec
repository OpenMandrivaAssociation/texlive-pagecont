Name:		texlive-pagecont
Version:	1.0
Release:	1
Summary:	Page numbering that continues between documents
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/pagecont
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pagecont.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pagecont.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pagecont.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The package provides the facility that several documents can be
typeset independently with page numbers in sequence, as if they
were a single document.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/pagecont/pagecont.sty
%doc %{_texmfdistdir}/doc/latex/pagecont/README
%doc %{_texmfdistdir}/doc/latex/pagecont/pagecont.pdf
#- source
%doc %{_texmfdistdir}/source/latex/pagecont/pagecont.dtx
%doc %{_texmfdistdir}/source/latex/pagecont/pagecont.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
