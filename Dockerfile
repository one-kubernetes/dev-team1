FROM openjdk:8
COPY . /usr/src/myapp
WORKDIR /usr/src/myapp
RUN ./mvnw clean package
CMD ["java", "-jar","target/spring-petclinic-2.4.5.jar"]