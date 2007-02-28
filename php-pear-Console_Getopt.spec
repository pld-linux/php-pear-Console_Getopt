%include	/usr/lib/rpm/macros.php
%define		_class		Console
%define		_subclass	Getopt
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}
Summary:	%{_pearname} - Command-line option parser
Summary(pl):	%{_pearname} - Parser opcji linii poleceñ
Name:		php-pear-%{_pearname}
Version:	1.2.2
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	88ac4fc1bf4e3b25c04198e19e9412e9
URL:		http://pear.php.net/package/Console_Getopt/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a PHP implementation of "getopt" supporting both short and
long options.

In PEAR status of this package is: %{_status}.

%description -l pl
Jest to PHP-owa implementacja "getopt" wspieraj±ca d³ugie i krótkie
opcje.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/*.php
