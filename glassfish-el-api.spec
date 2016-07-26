%global pkg_name glassfish-el-api
%{?scl:%scl_package %{pkg_name}}
%{?maven_find_provides_and_requires}

%global artifactId javax.el-api

Name:           %{?scl_prefix}%{pkg_name}
Version:        2.2.4
Release:        5.7%{?dist}
Summary:        Expression Language API 2.2.4

# Part of implementation files contain ASL 2.0 copyright
License:        CDDL and ASL 2.0
URL:            http://uel.java.net
# svn export https://svn.java.net/svn/uel~svn/tags/javax.el-api-2.2.4 javax.el-api-2.2.4
# tar cvJf javax.el-api-2.2.4.tar.xz javax.el-api-2.2.4/
Source0:        %{artifactId}-%{version}.tar.xz
Source1:        http://www.apache.org/licenses/LICENSE-2.0.txt
Source2:        generate_tarball.sh
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}javapackages-tools
BuildRequires:  %{?scl_prefix}jvnet-parent
BuildRequires:  %{?scl_prefix}maven-local
BuildRequires:  %{?scl_prefix}maven
BuildRequires:  %{?scl_prefix}maven-source-plugin

%description
This project provides an implementation of the Expression Language (EL). 
The main goals are:
 * Improves current implementation: bug fixes and performance improvements
 * Provides API for use by other tools, such as Netbeans

%package javadoc
Summary:        Javadoc for %{pkg_name}

%description javadoc
API documentation for %{pkg_name}.

%prep
%setup -q -n %{artifactId}-%{version}
%{?scl:scl enable %{scl} - <<"EOF"}
set -e -x
cp -p %{SOURCE1} .

%mvn_file : %{pkg_name}
%{?scl:EOF}

%build
%{?scl:scl enable %{scl} - <<"EOF"}
set -e -x
%mvn_build
%{?scl:EOF}

%install
%{?scl:scl enable %{scl} - <<"EOF"}
set -e -x
%mvn_install
%{?scl:EOF}

%files -f .mfiles
%doc LICENSE-2.0.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE-2.0.txt

%changelog
* Mon May 26 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.2.4-5.7
- Mass rebuild 2014-05-26

* Wed Feb 19 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.2.4-5.6
- Mass rebuild 2014-02-19

* Tue Feb 18 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.2.4-5.5
- Mass rebuild 2014-02-18

* Tue Feb 18 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.2.4-5.4
- Remove requires on java

* Mon Feb 17 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.2.4-5.3
- SCL-ize build-requires

* Thu Feb 13 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.2.4-5.2
- Rebuild to regenerate auto-requires

* Tue Feb 11 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.2.4-5.1
- First maven30 software collection build

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 2.2.4-5
- Mass rebuild 2013-12-27

* Fri Aug 23 2013 Michal Srb <msrb@redhat.com> - 2.2.4-4
- Migrate away from mvn-rpmbuild (Resolves: #997498)

* Fri Aug 02 2013 Michal Srb <msrb@redhat.com> - 2.2.4-3
- Add generate_tarball.sh script to SRPM

* Fri Jun 28 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.2.4-2
- Rebuild to regenerate API documentation
- Resolves: CVE-2013-1571

* Thu Jan 31 2013 David Xie <david.scriptfan@gmail.com> - 2.2.4-1
- Initial version of package
