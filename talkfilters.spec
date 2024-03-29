# TODO:
# - add libraries
# - dynamic linking with libraries?
Summary:	GNU Talk filters
Summary(pl.UTF-8):	Filtry tekstowe GNU
Name:		talkfilters
Version:	2.3.8
Release:	1
License:	GPL
Group:		Applications/Text
Source0:	http://www.hyperrealm.com/talkfilters/%{name}-%{version}.tar.gz
# Source0-md5:	c11c6863a1c246a8d49a80a1168b54c8
URL:		http://www.hyperrealm.com/talkfilters/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	flex
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Set of filters to text processing.

%description -l pl.UTF-8
Zestaw narzędzi do przetwarzania tekstu.

%prep
%setup -q

%build
cp -f /usr/share/automake/config.sub .
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_mandir}/man1,%{_bindir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p	/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	-p	/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man?/*
%{_infodir}/*.info*
