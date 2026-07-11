%global tl_name pagecont
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	Page numbering that continues between documents
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/pagecont
License:	lppl1.2
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pagecont.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pagecont.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pagecont.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides the facility that several documents can be typeset
independently with page numbers in sequence, as if they were a single
document.

