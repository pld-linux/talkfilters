Summary:	GNU Talk filters
Summary(pl):	Filtry tekstowe GNU
Name:		talkfilters
Version:	2.3.3
Release:	1
License:	GPL
Group:		Applications/Text
Source0:	http://www.dystance.net/software/talkfilters/%{name}-%{version}.tar.gz
# Source0-md5:	898c41682cd1cdfcb4ee1e52749f779b
Patch0:		%{name}-DESTDIR.patch
URL:		http://www.dystance.net/software/talkfilters/	
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
cp -f /usr/share/automake/config.sub .
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

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man?/*
