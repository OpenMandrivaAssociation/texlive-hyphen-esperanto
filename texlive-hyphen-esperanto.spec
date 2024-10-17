Name:		texlive-hyphen-esperanto
Version:	58652
Release:	2
Summary:	Esperanto hyphenation patterns
Group:		Publishing
URL:		https://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hyphen-esperanto.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-hyphen-base
Requires:	texlive-hyph-utf8

%description
Hyphenation patterns for Esperanto ISO Latin 3 and UTF-8
encodings. Note that TeX distributions don't ship any suitable
fonts in Latin 3 encoding, so unless you create your own font
support or want to use MlTeX, using native Unicode engines is
highly recommended.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/generic/hyph-utf8/loadhyph/*
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/*/*
%_texmf_language_dat_d/hyphen-esperanto
%_texmf_language_def_d/hyphen-esperanto
%_texmf_language_lua_d/hyphen-esperanto

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex %{buildroot}%{_texmfdistdir}

mkdir -p %{buildroot}%{_texmf_language_dat_d}
cat > %{buildroot}%{_texmf_language_dat_d}/hyphen-esperanto <<EOF
\%% from hyphen-esperanto:
esperanto loadhyph-eo.tex
EOF
perl -pi -e 's|\\%%|%%|;' %{buildroot}%{_texmf_language_dat_d}/hyphen-esperanto
mkdir -p %{buildroot}%{_texmf_language_def_d}
cat > %{buildroot}%{_texmf_language_def_d}/hyphen-esperanto <<EOF
\%% from hyphen-esperanto:
\addlanguage{esperanto}{loadhyph-eo.tex}{}{2}{2}
EOF
perl -pi -e 's|\\%%|%%|;' %{buildroot}%{_texmf_language_def_d}/hyphen-esperanto
mkdir -p %{buildroot}%{_texmf_language_lua_d}
cat > %{buildroot}%{_texmf_language_lua_d}/hyphen-esperanto <<EOF
-- from hyphen-esperanto:
	['esperanto'] = {
		loader = 'loadhyph-eo.tex',
		lefthyphenmin = 2,
		righthyphenmin = 2,
		synonyms = {  },
		patterns = 'hyph-eo.pat.txt',
		hyphenation = '',
	},
EOF
