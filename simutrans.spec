Name:		simutrans
Summary:	Transport and economic simulation game
Summary(pl):	Symulator transportowo - ekononomiczny
License:	Other License(s), see package
Group:		Applications/Games
Version:	0_81_19exp
Release:	1
Source0:	http://www.s-line.de/homepages/simutrans/data/simubase-%{version}.zip
Source1:	http://www.s-line.de/homepages/simutrans/data/simulinux-%{version}.tar.gz
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
Simutrans jest symulacj� transportowu i ekonomi z niekt�rymi aspektami
ekologii. Celem gry jest zbudowanie infrastruktury pozwalaj�cej na
transport d�br mi�dzy r�nymi zak�adami przemys�owymi i miastami, oraz
dostarczanie miastom wody i energii. Drugim celem jest zostanie tak
bogatym jak to tylko mo�liwe, przy czym trzeba reinwestowa� du�� cz��
zarobionych pieni�dzy w rozbudow� swojej sieci przemys�owej. Twoi
konkurenci nie �pi�!

%prep
%setup -q -n simutrans -b1

%build

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
%attr(755, root, root) %{_bindir}/*
%attr(755, root, root) %{_libdir}/%{name}/%{name}
%{_libdir}/%{name}/*.tab
%{_libdir}/%{name}/*.hex
%{_libdir}/%{name}/*.pa?
%{_libdir}/%{name}/*.fnt
%{_libdir}/%{name}/music
%{_libdir}/%{name}/sound
%{_libdir}/%{name}/text
%{_libdir}/%{name}/pak
