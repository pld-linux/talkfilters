Summary:	GNU Talk filters
Summary(pl):	Filtry tekstowe GNU
Name:		talkfilters
Version:	1.0
Release:	1
License:	GPL
Group:		Applications/Text
Source0:	ftp://ftp.gnu.org/pub/gnu/non-gnu/talkfilters/%{name}-%{version}.tar.gz
Patch0:		%{name}-DESTDIR.patch
BuildRequires:	flex
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Set of filters to text processing.

%description -l pl
Zestaw narz�dzi do przetwarzania tekstu.

%prep
%setup -q
%patch0 -p0

%build
%{__aclocal}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_mandir}/man1,%{_bindir}}
%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man?/*
