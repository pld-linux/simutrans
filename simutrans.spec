%define		fversion	%(echo %{version} | tr . - )
Summary:	Transport and economic simulation game
Summary(pl.UTF-8):	Symulator transportowo - ekonomiczny
Name:		simutrans
Version:	0.102.0
Release:	0.1
License:	Other License(s), see package
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/simutrans/simulinux_%{fversion}.zip
# Source0-md5:	9e81346c422a744cab97848c6f8ab7cb
Source1:	%{name}
Source2:	%{name}-redistribution.txt
Source3:	%{name}.desktop
URL:		http://www.simutrans.com/
ExclusiveArch:	%{ix86}
BuildRequires:	unzip
Requires:	SDL
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Simutrans is a transport and economic simulation which contains some
ecological aspects as well. The goal of the game is to build an
infrastructure which allows to transport goods between the various
industries and towns, and to supports the towns with water and energy.
A second goal is to become as rich as possible, but you'll have to
reinvest a good part of your earned cash to expand your
infrastructural network. Your competitors won't sleep!

%description -l pl.UTF-8
Simutrans jest symulacją transportu i ekonomii z niektórymi aspektami
ekologii. Celem gry jest zbudowanie infrastruktury pozwalającej na
transport dóbr między różnymi zakładami przemysłowymi i miastami, oraz
dostarczanie miastom wody i energii. Drugim celem jest zostanie tak
bogatym jak to tylko możliwe, przy czym trzeba reinwestować dużą część
zarobionych pieniędzy w rozbudowę swojej sieci przemysłowej.
Konkurenci nie śpią!

%prep
%setup -q -n simutrans 

%install
rm -rf $RPM_BUILD_ROOT
install -D %{SOURCE1} $RPM_BUILD_ROOT%{_bindir}/%{name}
install -d $RPM_BUILD_ROOT{%{_libdir}/%{name},%{_desktopdir}}
cp -a * $RPM_BUILD_ROOT%{_libdir}/%{name}
%{__rm} -rf $RPM_BUILD_ROOT%{_libdir}/%{name}/*.txt
install %{SOURCE2} .
install %{SOURCE3} $RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc change_request.txt problem_report.txt readme.txt thanks.txt copyright.txt %{name}-redistribution.txt
%attr(755,root,root) %{_bindir}/*
%dir %{_libdir}/%{name}
%attr(755,root,root) %{_libdir}/%{name}/%{name}
%{_desktopdir}/*.desktop
%{_libdir}/%{name}/*
