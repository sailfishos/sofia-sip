Name:       sofia-sip

Summary:    Sofia SIP User-Agent library
Version:    1.13.17
Release:    1

License:    LGPLv2+
URL:        https://github.com/freeswitch/sofia-sip
Source0:    %{name}-%{version}.tar.gz
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  make
BuildRequires:  libtool
BuildRequires:  pkgconfig(libssl) >= 0.9.7
BuildRequires:  pkgconfig(glib-2.0) >= 2.4

%description
Sofia SIP is a RFC-3261-compliant library for SIP user agents and
other network elements.  The Session Initiation Protocol (SIP) is an
application-layer control (signaling) protocol for creating,
modifying, and terminating sessions with one or more
participants. These sessions include Internet telephone calls,
multimedia distribution, and multimedia conferences.


%package glib
Summary:    Glib bindings for Sofia-SIP 
Requires:   %{name} = %{version}-%{release}

%description glib
GLib interface to Sofia SIP User Agent library.

%package utils
Summary:    Sofia-SIP Command Line Utilities
Requires:   %{name} = %{version}-%{release}

%description utils
Command line utilities for the Sofia SIP UA library.

%package glib-devel
Summary:    Glib bindings for Sofia SIP development files
Requires:   %{name}-glib = %{version}-%{release}
Requires:   %{name}-devel = %{version}-%{release}

%description glib-devel
Development package for Sofia SIP UA Glib library. This package
includes libraries and include files for developing glib programs
using Sofia SIP.

%package devel
Summary:    Sofia-SIP Development Package
Requires:   %{name} = %{version}-%{release}

%description devel
Development package for Sofia SIP UA library.

%package doc
Summary:   Documentation for %{name}
Requires:  %{name} = %{version}-%{release}

%description doc
Documentation for %{name}.


%prep
%autosetup -n %{name}-%{version}/%{name}

%build
%reconfigure --disable-static --without-doxygen --disable-stun
%make_build -Onone

%install
%make_install
find %{buildroot} -name \*.h.in -delete
find . -name installdox -delete

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%post glib -p /sbin/ldconfig

%postun glib -p /sbin/ldconfig

%files
%license COPYING COPYRIGHTS
%{_libdir}/libsofia-sip-ua.so.*

%files glib
%{_libdir}/libsofia-sip-ua-glib.so.*

%files utils
%{_bindir}/*

%files glib-devel
%{_includedir}/sofia-sip-*/sofia-sip/su_source.h
%{_libdir}/libsofia-sip-ua-glib.so
%{_libdir}/pkgconfig/sofia-sip-ua-glib.pc

%files devel
%dir %{_includedir}/sofia-sip-*
%dir %{_includedir}/sofia-sip-*/sofia-sip
%{_includedir}/sofia-sip-*/sofia-sip/*.h
%dir %{_includedir}/sofia-sip-*/sofia-resolv
%{_includedir}/sofia-sip-*/sofia-resolv/*.h
%{_libdir}/libsofia-sip-ua.so
%{_libdir}/pkgconfig/sofia-sip-ua.pc
%{_datadir}/sofia-sip

%files doc
%doc AUTHORS ChangeLog ChangeLog.ext-trees
%doc README README.developers RELEASE TODO
