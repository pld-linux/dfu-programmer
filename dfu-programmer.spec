Summary:	Atmel USB DFU programmer
Summary(pl.UTF-8):	Programator DFU dla układów Atmela z USB
Name:		dfu-programmer
Version:	0.5.4
Release:	1
License:	GPL v2+
Group:		Applications/System
Source0:	http://downloads.sourceforge.net/dfu-programmer/%{name}-%{version}.tar.gz
# Source0-md5:	707dcd0f957a74e92456ea6919faa772
Patch0:		%{name}-link.patch
URL:		http://dfu-programmer.sourceforge.net/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake
BuildRequires:	libusb-devel >= 1.0.0
BuildRequires:	pkgconfig >= 1:0.9.0
Requires:	libusb >= 1.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
dfu-programmer is an implementation of the Device Firmware Upgrade
class USB driver that enables firmware upgrades for various USB
enabled (with the correct bootloader) Atmel chips. This program was
created because the Atmel "FLIP" program for flashing devices does not
support flashing via USB on Linux, and because standard DFU loaders do
not work for Atmel's chips.

%description -l pl.UTF-8
dfu-programmer to implementacja sterownika USB klasy Device Firmware
Upgrade (uaktualniania firmware'u urządzeń), pozwalająca na
wykonywanie uaktualnień firmware'ów dla układów Atmela, obsługujących
USB i posiadających właściwy bootloader. Ten program powstał, ponieważ
program "FLIP" Atmela nie obsługuje urządzeń USB pod Linuksem, a
standardowe programy do DFU nie działają poprawnie z układami Atmela.

%prep
%setup -q
%patch0 -p1

%build
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/dfu-programmer
%{_mandir}/man1/dfu-programmer.1*
