/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.akka.social_network_emulator;

import akka.actor.AbstractActor;
import java.util.HashMap;
import java.util.Map;

/**
 *
 * @author PPyC - G2
 */
public class SocialMediaServerActor extends AbstractActor {
    private Map<String, String> messages = new HashMap<>();
    private Map<String, String> posts = new HashMap<>();
    private Map<String, String> followers = new HashMap<>();

    @Override
    public Receive createReceive() {
        return receiveBuilder()
            .match(Message.class, message -> {
                // Procesar y almacenar mensajes
                messages.put(message.getSender(), message.getMessage());
                System.out.println("Social Media Server: Nuevo mensaje de " + message.getSender() + ": " + message.getMessage());
            })
            .match(Post.class, post -> {
                // Procesar y almacenar publicaciones
                posts.put(post.getAuthor(), post.getMessage());
                System.out.println("Social Media Server: Nueva publicación de " + post.getAuthor() + ": " + post.getMessage());
            })
            .match(Follow.class, follow -> {
                // Procesar y almacenar seguidores
                followers.put(follow.getFollower(), follow.getTargetUser());
                System.out.println("Social Media Server: " + follow.getFollower() + " sigue a " + follow.getTargetUser());
            })
            .build();
    }

    // Define los mensajes que el actor SocialMediaServer puede recibir
    public static class Message {
        private final String sender;
        private final String message;

        public Message(String sender, String message) {
            this.sender = sender;
            this.message = message;
        }

        public String getSender() {
            return sender;
        }

        public String getMessage() {
            return message;
        }
    }

    public static class Post {
        private final String author;
        private final String message;

        public Post(String author, String message) {
            this.author = author;
            this.message = message;
        }

        public String getAuthor() {
            return author;
        }

        public String getMessage() {
            return message;
        }
    }

    public static class Follow {
        private final String follower;
        private final String targetUser;

        public Follow(String follower, String targetUser) {
            this.follower = follower;
            this.targetUser = targetUser;
        }

        public String getFollower() {
            return follower;
        }

        public String getTargetUser() {
            return targetUser;
        }
    }
}
