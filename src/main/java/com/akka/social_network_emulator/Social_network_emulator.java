/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 */

package com.akka.social_network_emulator;

import akka.actor.ActorRef;
import akka.actor.ActorSystem;
import akka.actor.Props;

/**
 *
 * @author PPyC - G2
 */
public class Social_network_emulator {

    public static void main(String[] args) {
        ActorSystem system = ActorSystem.create("SocialMediaSystem");

        // Crea un actor para el servidor de redes sociales
        ActorRef socialMediaServer = system.actorOf(Props.create(SocialMediaServerActor.class), "socialMediaServer");

        // Crea tres actores de usuario
        ActorRef user1 = system.actorOf(UserActor.props("Ana", socialMediaServer), "user1");
        ActorRef user2 = system.actorOf(UserActor.props("Carlos", socialMediaServer), "user2");
        ActorRef user3 = system.actorOf(UserActor.props("Sofia", socialMediaServer), "user3");

        // Simula las interacciones del guión
        // Escena 2: Reunión Virtual
        user1.tell(new UserActor.SendMessage("¡Hola amigos! ¿Por qué no nos reunimos virtualmente pronto?"), ActorRef.noSender());
        user2.tell(new UserActor.PostMessage("¡Eso suena genial! Podemos usar la videoconferencia de SocialNet."), ActorRef.noSender());
        user3.tell(new UserActor.SendMessage("¡Estoy emocionada por verlos a todos!"), ActorRef.noSender());

        // Escena 3: La Reunión Virtual
        user1.tell(new UserActor.SendMessage("Ha pasado tanto tiempo. ¿Qué están haciendo?"), ActorRef.noSender());
        user2.tell(new UserActor.PostMessage("¡Acabo de volver de un emocionante viaje por Tailandia!"), ActorRef.noSender());
        user3.tell(new UserActor.SendMessage("¡He estado trabajando en una nueva pieza de arte!"), ActorRef.noSender());
        user2.tell(new UserActor.FollowUser("Ana"), ActorRef.noSender());
        user1.tell(new UserActor.FollowUser("Carlos"), ActorRef.noSender());

        // Escena 4: Aventuras Compartidas
        user2.tell(new UserActor.PostMessage("Echa un vistazo a estas fotos de mi viaje a Tailandia."), ActorRef.noSender());
        user1.tell(new UserActor.SendMessage("¡Qué increíble viaje! ¿Cuál será tu próximo destino?"), ActorRef.noSender());
        user3.tell(new UserActor.PostMessage("Acabo de completar mi última obra de arte. ¡Espero que les guste!"), ActorRef.noSender());
        user2.tell(new UserActor.FollowUser("Sofia"), ActorRef.noSender());
        user1.tell(new UserActor.FollowUser("Sofia"), ActorRef.noSender());

        // Escena 6: Reunión en Persona
        user1.tell(new UserActor.SendMessage("¿Por qué no nos encontramos en el Café Amigos para ponernos al día en persona?"), ActorRef.noSender());
        user2.tell(new UserActor.SendMessage("¡Me parece una gran idea!"), ActorRef.noSender());
        user3.tell(new UserActor.SendMessage("¡Claro Vamos!"), ActorRef.noSender());

        // Detén el sistema después de un tiempo
        system.terminate();
    }

}
