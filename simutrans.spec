Summary:	Transport and economic simulation game
Summary(pl):	Symulator transportowo - ekononomiczny
Name:		simutrans
Version:	0_81_24exp
Release:	1
License:	Other License(s), see package
Group:		Applications/Games
Source0:	http://www.s-line.de/homepages/simutrans/data/simubase-%{version}.zip
Source1:	http://www.s-line.de/homepages/simutrans/data/simulinux-%{version}.tar.gz
# Source1-md5:	3a458f8d3220e1ba3943fe727152bb6d
Source2:	%{name}
URL:		http://www.simutrans.de/
ExclusiveArch:  %{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Simutrans is a transport and economic simulation which contains some
ecological aspects as well. The goal of the game is to build an
infrastructure which allows to transport goods between the various
industries and towns, and to supports the towns with water and energy.
A second goal is to become as rich as possible, but you'll have to
reinvest a good part of your earned cash to expand your
infrastructural network. Your competitors won't sleep!

%description -l pl
Simutrans jest symulacj± transportu i ekonomii z niektórymi aspektami
ekologii. Celem gry jest zbudowanie infrastruktury pozwalaj±cej na
transport dóbr miêdzy ró¿nymi zak³adami przemys³owymi i miastami, oraz
dostarczanie miastom wody i energii. Drugim celem jest zostanie tak
bogatym jak to tylko mo¿liwe, przy czym trzeba reinwestowaæ du¿± czê¶æ
zarobionych pieniêdzy w rozbudowê swojej sieci przemys³owej.
Konkurenci nie ¶pi±!

%prep
%setup -q -n simutrans -b1

%install
rm -rf $RPM_BUILD_ROOT
install -D %{SOURCE2} $RPM_BUILD_ROOT%{_bindir}/%{name}
install -d $RPM_BUILD_ROOT%{_libdir}/%{name}
cp -a * $RPM_BUILD_ROOT%{_libdir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc change_request.txt problem_report.txt readme.txt thanks.txt COPYRIGHT.txt
%attr(755,root,root) %{_bindir}/*
%dir %{_libdir}/%{name}
%attr(755,root,root) %{_libdir}/%{name}/%{name}
%{_libdir}/%{name}/*.tab
%{_libdir}/%{name}/*.hex
%{_libdir}/%{name}/*.pa?
%{_libdir}/%{name}/*.fnt
%{_libdir}/%{name}/music
%{_libdir}/%{name}/sound
%{_libdir}/%{name}/text
%{_libdir}/%{name}/pak
