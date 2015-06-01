Name:       sofia-sip

Summary:    Sofia SIP User-Agent library
Version:    1.12.11
Release:    2
Group:      Communications/Telephony and IM
License:    LGPLv2+
URL:        http://sofia-sip.sourceforge.net/
Source0:    http://dl.sourceforge.net/sofia-sip/%{name}-%{version}.tar.gz
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  pkgconfig(libssl) >= 0.9.7
BuildRequires:  pkgconfig(glib-2.0) >= 2.4
BuildRequires:  pkgconfig(check) >= 0.9.4

%description
Sofia SIP is a RFC-3261-compliant library for SIP user agents and
other network elements.  The Session Initiation Protocol (SIP) is an
application-layer control (signaling) protocol for creating,
modifying, and terminating sessions with one or more
participants. These sessions include Internet telephone calls,
multimedia distribution, and multimedia conferences.


%package glib
Summary:    Glib bindings for Sofia-SIP
Group:      Communications/Telephony and IM
Requires:   %{name} = %{version}-%{release}
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig

%description glib
GLib interface to Sofia SIP User Agent library.

%package utils
Summary:    Sofia-SIP Command Line Utilities
Group:      Applications/Internet
Requires:   %{name} = %{version}-%{release}

%description utils
Command line utilities for the Sofia SIP UA library.

%package glib-devel
Summary:    Glib bindings for Sofia SIP development files
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}
Requires:   sofia-sip-glib = %{version}-%{release}
Requires:   sofia-sip-devel = %{version}-%{release}

%description glib-devel
Development package for Sofia SIP UA Glib library. This package
includes libraries and include files for developing glib programs
using Sofia SIP.


%package devel
Summary:    Sofia-SIP Development Package
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}

%description devel
Development package for Sofia SIP UA library.

%prep
%setup -q -n %{name}-%{version}/src

%build
%configure --disable-static
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
%make_install

find %{buildroot} -name \*.h.in -delete

%check
#TPORT_DEBUG=9 TPORT_TEST_HOST=0.0.0.0 make check

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%post glib -p /sbin/ldconfig

%postun glib -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog ChangeLog.ext-trees COPYING COPYRIGHTS
%doc README README.developers RELEASE TODO
%{_libdir}/libsofia-sip-ua.so.*

%files glib
%defattr(-,root,root,-)
%{_libdir}/libsofia-sip-ua-glib.so.*

%files utils
%defattr(-,root,root,-)
%{_bindir}/*
%{_mandir}/man1/*.1*

%files glib-devel
%defattr(-,root,root,-)
%{_includedir}/sofia-sip-1.12/sofia-sip/su_source.h
%{_libdir}/libsofia-sip-ua-glib.so
%{_libdir}/pkgconfig/sofia-sip-ua-glib.pc

%files devel
%defattr(-,root,root,-)
%dir %{_includedir}/sofia-sip-1.12
%dir %{_includedir}/sofia-sip-1.12/sofia-sip
%{_includedir}/sofia-sip-1.12/sofia-sip/*.h
%exclude %{_includedir}/sofia-sip-1.12/sofia-sip/su_source.h
%dir %{_includedir}/sofia-sip-1.12/sofia-resolv
%{_includedir}/sofia-sip-1.12/sofia-resolv/*.h
%{_libdir}/libsofia-sip-ua.so
%{_libdir}/pkgconfig/sofia-sip-ua.pc
%{_datadir}/sofia-sip
