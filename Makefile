PKG_NAME := jdk-javacc
URL := http://repo1.maven.org/maven2/net/java/dev/javacc/javacc/4.2/javacc-4.2.jar
ARCHIVES := http://repo1.maven.org/maven2/net/java/dev/javacc/javacc/4.2/javacc-4.2.pom %{buildroot}

include ../common/Makefile.common
