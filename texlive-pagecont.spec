Name:		texlive-pagecont
Version:	15878
Release:	2
Summary:	Page numbering that continues between documents
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/pagecont
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pagecont.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pagecont.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pagecont.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides the facility that several documents can be
typeset independently with page numbers in sequence, as if they
were a single document.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
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
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
