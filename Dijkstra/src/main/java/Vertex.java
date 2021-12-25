/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author A. Enes
 */
class Vertex implements Comparable<Vertex>
{
    public final int name;
    public Edge[] adjacencies;
    public double minDistance = Double.POSITIVE_INFINITY;
    public Vertex previous;
    public Vertex(int argName) { name = argName; }

    @Override
    public String toString() {
        return "=>" + name + "=>";
    }
    
    
    public int compareTo(Vertex other)
    {
        return Double.compare(minDistance, other.minDistance);
    }

}
