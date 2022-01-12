#
# Conditional build:
%bcond_without	ocaml_opt	# native optimized binaries (bytecode is always built)

# not yet available on x32 (ocaml 4.02.1), update when upstream will support it
%ifnarch %{ix86} %{x8664} %{arm} aarch64 ppc sparc sparcv9
%undefine	with_ocaml_opt
%endif

Summary:	Platform-independent core of Async RPC library
Summary(pl.UTF-8):	Generowanie funkcji porównujących z typów
Name:		ocaml-async_rpc_kernel
Version:	0.14.0
Release:	1
License:	MIT
Group:		Libraries
#Source0Download: https://github.com/janestreet/async_rpc_kernel/tags
Source0:	https://github.com/janestreet/async_rpc_kernel/archive/v%{version}/async_rpc_kernel-%{version}.tar.gz
# Source0-md5:	4756357da73f152705a5e954fd1926b2
URL:		https://github.com/janestreet/async_rpc_kernel
BuildRequires:	ocaml >= 1:4.08.0
BuildRequires:	ocaml-async_kernel-devel >= 0.14
BuildRequires:	ocaml-async_kernel-devel < 0.15
BuildRequires:	ocaml-core_kernel-devel >= 0.14
BuildRequires:	ocaml-core_kernel-devel < 0.15
BuildRequires:	ocaml-dune >= 2.0.0
BuildRequires:	ocaml-ppx_jane-devel >= 0.14
BuildRequires:	ocaml-ppx_jane-devel < 0.15
BuildRequires:	ocaml-protocol_version_header-devel >= 0.14
BuildRequires:	ocaml-protocol_version_header-devel < 0.15
%requires_eq	ocaml-runtime
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		debug_package	%{nil}

%description
Platform-independent core of Async RPC library.

This package contains files needed to run bytecode executables using
async_rpc_kernel library.

%description -l pl.UTF-8
Generowanie funkcji porównujących z typów.

Pakiet ten zawiera binaria potrzebne do uruchamiania programów
używających biblioteki async_rpc_kernel.

%package devel
Summary:	Platform-independent core of Async RPC library - development part
Summary(pl.UTF-8):	Niezależna od platformy podstawa biblioteki Async RPC - część programistyczna
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
%requires_eq	ocaml
Requires:	ocaml-async_kernel-devel >= 0.14
Requires:	ocaml-core_kernel-devel >= 0.14
Requires:	ocaml-ppx_jane-devel >= 0.14
Requires:	ocaml-protocol_version_header-devel >= 0.14

%description devel
This package contains files needed to develop OCaml programs using
async_rpc_kernel library.

%description devel -l pl.UTF-8
Pakiet ten zawiera pliki niezbędne do tworzenia programów w OCamlu
używających biblioteki async_rpc_kernel.

%prep
%setup -q -n async_rpc_kernel-%{version}

%build
dune build --verbose

%install
rm -rf $RPM_BUILD_ROOT

dune install --destdir=$RPM_BUILD_ROOT

# sources
%{__rm} $RPM_BUILD_ROOT%{_libdir}/ocaml/async_rpc_kernel/*.ml
# packaged as %doc
%{__rm} -r $RPM_BUILD_ROOT%{_prefix}/doc/async_rpc_kernel

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES.md LICENSE.md
%dir %{_libdir}/ocaml/async_rpc_kernel
%{_libdir}/ocaml/async_rpc_kernel/META
%{_libdir}/ocaml/async_rpc_kernel/*.cma
%if %{with ocaml_opt}
%attr(755,root,root) %{_libdir}/ocaml/async_rpc_kernel/*.cmxs
%endif

%files devel
%defattr(644,root,root,755)
%{_libdir}/ocaml/async_rpc_kernel/*.cmi
%{_libdir}/ocaml/async_rpc_kernel/*.cmt
%{_libdir}/ocaml/async_rpc_kernel/*.cmti
%{_libdir}/ocaml/async_rpc_kernel/*.mli
%if %{with ocaml_opt}
%{_libdir}/ocaml/async_rpc_kernel/async_rpc_kernel.a
%{_libdir}/ocaml/async_rpc_kernel/*.cmx
%{_libdir}/ocaml/async_rpc_kernel/*.cmxa
%endif
%{_libdir}/ocaml/async_rpc_kernel/dune-package
%{_libdir}/ocaml/async_rpc_kernel/opam
