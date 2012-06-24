%include	/usr/lib/rpm/macros.php
%define		_class		Console
%define		_subclass	Getopt
%define		_pearname	%{_class}_%{_subclass}
Summary:	%{_pearname} - Command-line option parser
Summary(pl):	%{_pearname} - Parser opcji linii polece�
Name:		php-pear-%{_pearname}
Version:	1.0
Release:	2
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
URL:		http://pear.php.net/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a PHP implementation of "getopt" supporting both short and
long options.

%description -l pl
Jest to PHPowa implementacja "getopt" wspieraj�ca d�ugie i kr�tkie
opcje.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

install %{_pearname}-%{version}/%{_class}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{php_pear_dir}/%{_class}/*.php
