%include	/usr/lib/rpm/macros.php
%define		_class		Console
%define		_subclass	Getopt
%define		_pearname	%{_class}_%{_subclass}
Summary:	%{_class}_%{_subclass} - Command-line option parser
Summary(pl):	%{_class}_%{_subclass} - Parser opcji linii poleceñ
Name:		php-pear-%{_pearname}
Version:	0.11
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
BuildRequires:	rpm-php-pearprov
URL:		http://pear.php.net/
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a PHP implementation of "getopt" supporting both short and
long options.

%description -l pl
Jest to PHPowa implementacja "getopt" wspieraj±ca d³ugie i krótkie
opcje.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
cd %{_pearname}-%{version}

install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

install %{_class}/*.php		$RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{php_pear_dir}/%{_class}/*.php
