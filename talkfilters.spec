Summary:	GNU Talk filters
Summary(pl):	Filtry tekstowe GNU
Name:		talkfilters
Version:	1.0
Release:	1
License:	GPL
Group:		Applications/Text
Source0:	ftp://ftp.gnu.org/pub/gnu/non-gnu/talkfilters/%{name}-%{version}.tar.gz
BuildRequires:	flex
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Set of filters to text processing.

%description -l pl
Zestaw narzêdzi do przetwarzania tekstu.

%prep
%setup -q -c

%build
%{__make} CFLAGS="%{rpmcflags}" LEXLIB="-lfl"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install jive valspeak homo kraut chef redneck $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README

%attr(755,root,root) %{_bindir}/*
