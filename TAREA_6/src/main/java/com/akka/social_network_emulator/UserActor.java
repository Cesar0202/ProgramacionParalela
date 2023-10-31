/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.akka.social_network_emulator;

import akka.actor.AbstractActor;
import akka.actor.ActorRef;
import akka.actor.Props;
import com.akka.social_network_emulator.SocialMediaServerActor.Follow;
import com.akka.social_network_emulator.SocialMediaServerActor.Message;
import com.akka.social_network_emulator.SocialMediaServerActor.Post;

/**
 *
 * @author PPyC - G2
 */
public class UserActor extends AbstractActor {
    private final String username;
    private final ActorRef socialMediaServer;

    public UserActor(String username, ActorRef socialMediaServer) {
        this.username = username;
        this.socialMediaServer = socialMediaServer;
    }

    public static Props props(String username, ActorRef socialMediaServer) {
        return Props.create(UserActor.class, () -> new UserActor(username, socialMediaServer));
    }

    @Override
    public Receive createReceive() {
        return receiveBuilder()
            .match(SendMessage.class, message -> {
                // Simular enviar un mensaje
                socialMediaServer.tell(new Message(username, message.getMessage()), getSelf());
            })
            .match(PostMessage.class, post -> {
                // Simular hacer una publicación
                socialMediaServer.tell(new Post(username, post.getMessage()), getSelf());
            })
            .match(FollowUser.class, follow -> {
                // Simular seguir a otro usuario
                socialMediaServer.tell(new Follow(username, follow.getTargetUser()), getSelf());
            })
            .build();
    }

    // Define los mensajes que el actor User puede recibir
    public static class SendMessage {
        private final String message;

        public SendMessage(String message) {
            this.message = message;
        }

        public String getMessage() {
            return message;
        }
    }

    public static class PostMessage {
        private final String message;

        public PostMessage(String message) {
            this.message = message;
        }

        public String getMessage() {
            return message;
        }
    }

    public static class FollowUser {
        private final String targetUser;

        public FollowUser(String targetUser) {
            this.targetUser = targetUser;
        }

        public String getTargetUser() {
            return targetUser;
        }
    }
}