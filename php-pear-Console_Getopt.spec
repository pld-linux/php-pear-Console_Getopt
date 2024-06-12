#
# Conditional build:
%bcond_with	bootstrap	# bootstrap build without PEAR installed (for first php-pear-PEAR installation)

%define		status		stable
%define		pearname	Console_Getopt
Summary:	%{pearname} - Command-line option parser
Summary(pl.UTF-8):	%{pearname} - Parser opcji linii poleceń
Name:		php-pear-%{pearname}
Version:	1.4.3
Release:	2
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{pearname}-%{version}.tgz
# Source0-md5:	78620b71acdf113968c3482845bcbbc2
URL:		http://pear.php.net/package/Console_Getopt/
%if %{without bootstrap}
BuildRequires:	php-pear-PEAR
%endif
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear
Requires:	rpm-whiteout
Conflicts:	rpm-whiteout < 1.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a PHP implementation of "getopt" supporting both short and
long options.

In PEAR status of this package is: %{status}.

%description -l pl.UTF-8
Jest to PHP-owa implementacja "getopt" wspierająca długie i krótkie
opcje.

Ta klasa ma w PEAR status: %{status}.

%prep
%if %{without bootstrap}
%pear_package_setup
%else
%setup -q -c -n %{pearname}-%{version}
%{__mv} %{pearname}-%{version}/* .
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}

%if %{without bootstrap}
%pear_package_install
%else
cp -pr Console $RPM_BUILD_ROOT%{php_pear_dir}
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%if %{without bootstrap}
%doc install.log
%{php_pear_dir}/.registry/console_getopt.reg
%endif
%{php_pear_dir}/Console/Getopt.php
