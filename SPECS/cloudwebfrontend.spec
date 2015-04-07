Name:           cloudwebfrontend
Version:        1.2
Release:        1%{?dist}
Summary:        The cloud web front end 
License:        GPLv2
Source0:        cloudwebfrontend.tar.gz   
BuildArch:      noarch
Requires:       python-cherrypy = 3.2.2, python-ldap = 2.3.10, python-jinja2 = 2.2.1, python-websockify = 0.5.1, numpy = 1.4.1, words
Requires(pre):  /usr/sbin/useradd, /usr/bin/getent
Requires(postun): /usr/sbin/userdel

%description
This package contains the code for the SCD cloud web frontend.

%prep
echo "Prep"
%setup -q

%build
echo "Build"

%install
echo "Install"
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/var/www/frontend/
cp -Ra . $RPM_BUILD_ROOT/var/www/frontend/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,cloud,cloud,)
/var/www/frontend
%defattr(-,cloud,cloud,777)
/var/www/frontend/tokens

%pre
/usr/bin/getent group cloud || /usr/sbin/groupadd -r cloud
/usr/bin/getent passwd cloud || /usr/sbin/useradd -N -r -d /var/www/frontend -s /sbin/nologin cloud

%postun
/usr/sbin/userdel cloud

%changelog

