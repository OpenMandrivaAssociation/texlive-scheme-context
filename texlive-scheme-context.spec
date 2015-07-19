# revision 32062
# category Scheme
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-scheme-context
Version:	20131201
Release:	9
Summary:	ConTeXt scheme
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/scheme-context.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-context
Requires:	texlive-collection-context
Requires:	texlive-collection-metapost
Requires:	texlive-tex-gyre
Requires:	texlive-tex-gyre-math
Requires:	texlive-antt
Requires:	texlive-iwona
Requires:	texlive-kurier
Requires:	texlive-poltawski
Requires:	texlive-xits
Requires:	texlive-Asana-Math
Requires:	texlive-gentium-tug
Requires:	texlive-txfonts
Requires:	texlive-pxfonts
Requires:	texlive-eulervm
Requires:	texlive-marvosym
Requires:	texlive-wasy
Requires:	texlive-ccicons
Requires:	texlive-ly1

%description
This is the TeX Live scheme for installing ConTeXt.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install
