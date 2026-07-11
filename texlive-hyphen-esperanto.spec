%global tl_name hyphen-esperanto
%global tl_revision 78069

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Esperanto hyphenation patterns.
Group:		Publishing
URL:		https://www.ctan.org/pkg/hyphen-esperanto
License:	LPPL
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hyphen-esperanto.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(hyph-utf8)
Requires:	texlive(hyphen-base)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Hyphenation patterns for Esperanto ISO Latin 3 and UTF-8 encodings. Note
that TeX distributions don't ship any suitable fonts in Latin 3
encoding, so unless you create your own font support or want to use
MlTeX, using native Unicode engines is highly recommended.

