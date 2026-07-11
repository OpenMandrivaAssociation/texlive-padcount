%global tl_name padcount
%global tl_revision 47621

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	Pad numbers with arbitrary characters
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/padcount
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/padcount.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/padcount.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/padcount.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides some simple macros which will pad numbers (or,
indeed, any expanded token) with your choice of character (defaulting to
"0") to your choice of number of places (defaults to "2"). This works
not only on arabic numerals, but on any expanded list of tokens passed
to it. This makes it suitable for, among other things, counters of all
kinds.

