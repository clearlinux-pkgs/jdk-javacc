Name     : jdk-javacc
Version  : 4.2
Release  : 1
URL      : http://repo1.maven.org/maven2/net/java/dev/javacc/javacc/4.2/javacc-4.2.jar
Source0  : http://repo1.maven.org/maven2/net/java/dev/javacc/javacc/4.2/javacc-4.2.jar
Source1  : http://repo1.maven.org/maven2/net/java/dev/javacc/javacc/4.2/javacc-4.2.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-2-Clause
Requires: jdk-javacc-data
BuildRequires : javapackages-tools
BuildRequires : lxml
BuildRequires : openjdk-dev
BuildRequires : python3
BuildRequires : six

%description
No detailed description available

%package data
Summary: data components for the jdk-javacc package.
Group: Data

%description data
data components for the jdk-javacc package.


%prep

%build

%install
mkdir -p %{buildroot}/usr/share/maven-poms
mkdir -p %{buildroot}/usr/share/maven-metadata
mkdir -p %{buildroot}/usr/share/java

mv %{SOURCE0} %{buildroot}/usr/share/java/javacc.jar
mv %{SOURCE1} %{buildroot}/usr/share/maven-poms/javacc.pom

# Creates metadata
python3 /usr/share/java-utils/maven_depmap.py \
-n "" \
--pom-base %{buildroot}/usr/share/maven-poms \
--jar-base %{buildroot}/usr/share/java \
%{buildroot}/usr/share/maven-metadata/javacc.xml \
%{buildroot}/usr/share/maven-poms/javacc.pom \
%{buildroot}/usr/share/java/javacc.jar \

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/javacc.jar
/usr/share/maven-metadata/javacc.xml
/usr/share/maven-poms/javacc.pom
