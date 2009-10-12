Summary:	Bigelow & Holmes Lucida Typewriter 100dpi bitmap fonts
Summary(pl.UTF-8):	Fonty bitmapowe 100dpi Bigelow & Holmes Lucida Typewriter
Name:		xorg-font-font-bh-lucidatypewriter-100dpi
Version:	1.0.1
Release:	1
License:	MIT
Group:		Fonts
Source0:	http://xorg.freedesktop.org/releases/individual/font/font-bh-lucidatypewriter-100dpi-%{version}.tar.bz2
# Source0-md5:	a2b3951dbc6ddb2e4c7e09519dd13333
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-app-bdftopcf
BuildRequires:	xorg-app-mkfontdir
BuildRequires:	xorg-app-mkfontscale
BuildRequires:	xorg-font-font-util >= 1.1.1
BuildRequires:	xorg-util-util-macros
Requires(post,postun):	fontpostinst
Requires:	%{_fontsdir}/100dpi
# contains useful aliases for these fonts
Requires:	xorg-font-font-alias >= 1.0.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Bigelow & Holmes Lucida Typewriter 100dpi bitmap fonts.

This package includes Unicode fonts as well as in ISO-8859-1,
ISO-8859-2, ISO-8859-3, ISO-8859-4, ISO-8859-9, ISO-8859-10,
ISO-8859-13, ISO-8859-14 and ISO-8859-15 encodings.

%description -l pl.UTF-8
Fonty bitmapowe 100dpi Bigelow & Holmes Lucida Typewriter.

Ten pakiet zawiera fonty unikodowe, a także w kodowaniach ISO-8859-1,
ISO-8859-2, ISO-8859-3, ISO-8859-4, ISO-8859-9, ISO-8859-10,
ISO-8859-13, ISO-8859-14 i ISO-8859-15.

%prep
%setup -q -n font-bh-lucidatypewriter-100dpi-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--build=%{_host_platform} \
	--host=%{_host_platform} \
	--with-fontdir=%{_fontsdir}/100dpi

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post
fontpostinst 100dpi

%postun
fontpostinst 100dpi

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog
%{_fontsdir}/100dpi/lut*.pcf.gz
