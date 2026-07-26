%define upstream_name    Catalyst-View-GD
Name:		perl-%{upstream_name}
Version:	0.01
Release:	7

Summary:	A Catalyst View for GD images
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/Catalyst-View-GD
Source0:	https://cpan.metacpan.org/authors/id/S/ST/STEVAN/Catalyst-View-GD-%{version}.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl(Catalyst::Runtime)
BuildRequires:	perl(GD)
BuildRequires:	perl(Test::Exception)
BuildRequires:	perl(Test::Image::GD)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Module::Build::Compat)
BuildArch:	noarch

%description
This is a Catalyst View subclass which can handle rendering GD based image
content. 

%prep
%setup -q -n %{upstream_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes META.yml README
%{_mandir}/man3/*
%perl_vendorlib/*

