Name:		texlive-padcount
Version:	47621
Release:	1
Summary:	Pad numbers with arbitrary characters
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/padcount
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/padcount.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/padcount.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/padcount.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides some simple macros which will pad numbers
(or, indeed, any expanded token) with your choice of character
(defaulting to "0") to your choice of number of places
(defaults to "2"). This works not only on arabic numerals, but
on any expanded list of tokens passed to it. This makes it
suitable for, among other things, counters of all kinds.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/padcount
%{_texmfdistdir}/tex/latex/padcount
%doc %{_texmfdistdir}/doc/latex/padcount

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
