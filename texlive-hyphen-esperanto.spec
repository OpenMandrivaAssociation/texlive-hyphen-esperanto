%global tl_name hyphen-esperanto
%global tl_revision 78069

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	2
Summary:	Esperanto hyphenation patterns.
Group:		Publishing
URL:		https://www.ctan.org/pkg/hyphen-esperanto
License:	LPPL
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hyphen-esperanto.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(hyph-utf8)
Requires:	texlive(hyphen-base)
Requires:	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{version}

%description
Hyphenation patterns for Esperanto ISO Latin 3 and UTF-8 encodings. Note
that TeX distributions don't ship any suitable fonts in Latin 3
encoding, so unless you create your own font support or want to use
MlTeX, using native Unicode engines is highly recommended.


%install -a
mkdir -p %{buildroot}%{_texmf_language_dat_d}
cat > %{buildroot}%{_texmf_language_dat_d}/%{tl_name} <<'TL_HYPHEN_EOF'
% from hyphen-esperanto:
esperanto loadhyph-eo.tex
TL_HYPHEN_EOF
mkdir -p %{buildroot}%{_texmf_language_def_d}
cat > %{buildroot}%{_texmf_language_def_d}/%{tl_name} <<'TL_HYPHEN_EOF'
% from hyphen-esperanto:
\addlanguage{esperanto}{loadhyph-eo.tex}{}{2}{2}
TL_HYPHEN_EOF
mkdir -p %{buildroot}%{_texmf_language_lua_d}
cat > %{buildroot}%{_texmf_language_lua_d}/%{tl_name} <<'TL_HYPHEN_EOF'
-- from hyphen-esperanto:
['esperanto'] = {
	loader = 'loadhyph-eo.tex',
	lefthyphenmin = 2,
	righthyphenmin = 2,
	synonyms = {  },
	patterns = 'hyph-eo.pat.txt',
},
TL_HYPHEN_EOF
