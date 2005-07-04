# TODO:
# - add libraries
# - dynamic linking with libraries?
Summary:	GNU Talk filters
Summary(pl):	Filtry tekstowe GNU
Name:		talkfilters
Version:	2.3.4
Release:	1
License:	GPL
Group:		Applications/Text
Source0:	http://www.dystance.net/software/talkfilters/%{name}-%{version}.tar.gz
# Source0-md5:	58048954f867628f098bc4f09f9672ad
Patch0:		%{name}-DESTDIR.patch
URL:		http://www.dystance.net/software/talkfilters/	
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	flex
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Set of filters to text processing.

%description -l pl
Zestaw narzêdzi do przetwarzania tekstu.

%prep
%setup -q
%patch0 -p0

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

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man?/*
%{_infodir}/*.info*
