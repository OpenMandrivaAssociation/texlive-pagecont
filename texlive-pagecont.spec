# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/pagecont
# catalog-date 2009-11-10 09:17:41 +0100
# catalog-license lppl
# catalog-version 1.0
Name:		texlive-pagecont
Version:	1.0
Release:	3
Summary:	Page numbering that continues between documents
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/pagecont
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pagecont.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pagecont.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pagecont.source.tar.xz
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.0-2
+ Revision: 754617
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.0-1
+ Revision: 719180
- texlive-pagecont
- texlive-pagecont
- texlive-pagecont
- texlive-pagecont

