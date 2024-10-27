## Java의 구동 원리와 JDK

---

### Java

Java의 가장 큰 특징은 플랫폼에 독립적인 언어라는 점이다. 소스 코드를 기계어로 직접 컴파일하여 링크하는 `C/C++`의 컴파일러와 달리 자바 컴파일러는 바이트코드인 클래스 파일(`.class`)을 생성하고, 이 파일의 바이트코드를 읽은 뒤 기계어로 바꾸어 실행하는 것은 JVM(Java Virtual Machine)이다.

<div align="center">
  <img width="600" alt="java_1" src="https://github.com/user-attachments/assets/5ddef792-46a6-4970-98e5-6ceca7649692">
</div>

자바는 표준 스펙과 구현체로 나눌 수 있다. 표준 스펙의 경우 자바는 이렇게 만들어야 한다는 일종의 설계도이다. 이 표준 스펙을 기반으로 여러 회사에서 실제 작동하는 자바를 만든다. 자바 표준 스펙은 자바 커뮤니티 프로세스(JCP)를 통해 관리된다. 자바 구현들은 모두 표준 스펙에 맞도록 개발되어있기에 오라클의 Open JDK를 사용하다가 Amazon Corretto 자바로 변경해도 대부분 문제없이 동작한다.

<div align="center">
  <img width="600" alt="java_2" src="https://github.com/user-attachments/assets/87deef8d-ce53-4b44-9213-67a62edfbb29">
</div>

<div align="center">
  <img width="600" alt="java_3" src="https://github.com/user-attachments/assets/b7dc4e95-2ff3-4409-a98e-8bd2144d0fc3">
</div>

Java는 컴파일 단계와 실행 단계로 나누어진다.

- 컴파일
  - `javac`라는 프로그램을 통해 이루어진다.
  - `.java` 파일을 `.class` 파일로 컴파일한다.
  - `javac Hello.java`
  - Intellij의 경우 `out` 폴더에서 컴파일된 `.class` 파일을 확인할 수 있다.

- 실행
  - `java`라는 프로그램을 사용하며, 컴파일된 `.class` 파일을 지정해준다.
  - `java Hello` (확장자는 제외한다.)

이러한 특성으로 인해 자바는 운영체제에 독립적이다. OS 호환성 문제는 자바가 해결해준다. 서버는 주로 리눅스를 사용하며, 만약 AWS를 사용한다면 Amazon Corretto 자바를 AWS 리눅스 서버에 설치하고, 개발 시 컴파일한 `.class` 파일을 서버에 배포하면된다.

### JDK (Java Development Kit)

Java 프로그램을 개발하기 위해 필요한 도구 모음이다. Java 컴파일러, 디버깅 도구, 자바 가상 머신(JVM) 등을 포함한다.

#### JDK의 종류

> Java SE : Java Platform, Standard Edition<br>
표준 자바 플랫폼으로 표준적인 컴퓨팅 환경을 지원하기 위한 자바 가상머신 규격 및 API 집합을 포함한다.<br>
JavaEE, JavaME는 구체적인 목적에 따라 자바 SE를 기반으로 API를 추가하거나 자바 가상머신 규격 및 API의 일부를 택하여 정의된다.

> Java EE: Java Platform, Enterprise Edition<br>
JavaSE에 웹 어플리케이션 서버에서 동작하는 기능을 추가한 플랫폼이다.<br>
이 스펙에 따라 제품을 구현한 것을 웹 어플리케이션 서버(WAS)라 한다. e.g) Tomcat

> Java ME: Java Platform, Micro Edition<br>
제한된 자원을 가진 휴대전화, PDA 등에서 Java 프로그래밍 언어를 지원하기 위해 만든 플랫폼 중 하나이다.

#### JDK의 구성

<div align="center">
  <img width="600" alt="java_4" src="https://github.com/user-attachments/assets/f1310d72-bb86-4bc1-af7b-c193e170b46a">
</div>

- `javac`: 자바 컴파일러 (자바 소스파일 -> 바이트 코드로 변환)

- `java`: javac가 만든 클래스 파일을 해석 및 실행

- `JDB`: 자바 디버깅 툴

- `JRE`: Java 런타임 환경은 Java 프로그램이 올바르게 실행되기 위해 필요한 소프트웨어이며, 자바 코드를 실행하기 위한 도구들로 구성된 패키지이다. Java는 여러 최신 웹 및 모바일 애플리케이션의 기반이 되는 컴퓨터 언어이며, JRE는 Java 프로그램과 운영 체제 간의 통신을 위한 기본 기술이다. JRE는 Java 소프트웨어 작성 시 추가 수정없이 어떤 운영 체제에서도 실행되도록 모든 리소스를 제공하는 번역기 및 촉진자 역할을 한다.

- `JVM`: 자바 가상 머신은 자바 프로그램 실행환경을 만들어 주는 소프트웨어다. 자바 코드를 컴파일하여 `.class` 바이트 코드로 만들면 이 코드가 자바 가상 머신 환경에서 실행된다. JVM은 JRE(Java Runtime Environment)에 포함되어있으며, 현재 사용하는 컴퓨터의 운영체제에 맞는 자바 실행환경(JRE)이 설치되어 있다면 자바 가상 머신이 설치되어 있다는 뜻이다.

요약하자면 다음과 같다.

JDK는 Java 프로그램을 개발하기 위해 필요한 도구 모음이다. JRE는 구현한 프로그램들을 런타임 할 수 있도록 도와주는 프로그램이다.
JVM은 운영체제와 하드웨어의 환경에 맞춰 실행시켜주는 프로그램이다. (참고) IDE(Integrated Development Environment)는 코딩, 디버그, 컴파일, 배포 등 프로그램 개발에 관련된 모든 작업을 하나의 프로그램 안에서 처리하는 것을 도와주는 소프트웨어이다.
