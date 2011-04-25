%include	/usr/lib/rpm/macros.php
%define		_status		stable
%define		_pearname	Console_Getopt
Summary:	%{_pearname} - Command-line option parser
Summary(pl.UTF-8):	%{_pearname} - Parser opcji linii poleceń
Name:		php-pear-%{_pearname}
Version:	1.3.1
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	310b39cf091b9a0abf398bead60f3f8d
URL:		http://pear.php.net/package/Console_Getopt/
BuildRequires:	php-pear-PEAR
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

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Jest to PHP-owa implementacja "getopt" wspierająca długie i krótkie
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
%{php_pear_dir}/Console/*.php
