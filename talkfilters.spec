Summary:	GNU Talk filters
Summary(pl):	Filtry tekstowe GNU
Name:		talkfilters
Version:	2.3.2
Release:	1
License:	GPL
Group:		Applications/Text
Source0:	http://www.dystance.net/software/talkfilters/%{name}-%{version}.tar.gz
# Source0-md5:	e5f773423979f845c42f7f777e1b8916
Url:		http://www.dystance.net/software/talkfilters/	
Patch0:		%{name}-DESTDIR.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	flex
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Set of filters to text processing.

%description -l pl
Zestaw narzêdzi do przetwarzania tekstu.

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
